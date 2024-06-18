import time
from typing import Dict, List

from backends.contracts_executor import ContractsExecutor
from backends.tonapi import TonapiAdapter
from models.backend import CalculationBackend
import requests
from models.results import ProjectStat, CalculationResults
from models.season_config import SeasonConfig, DexPool
import psycopg2
import psycopg2.extras
from loguru import logger

"""
DeFi leaderboard based on DeFiLlama and tonapi:
1. Requests history TVL for the projects
2. Excludes boosted pools, whitelisted in the season config using tonapi (to get pool states) and
pool's get method invocation
"""
class DefillamaDeFiBackend(CalculationBackend):
    # DEX pool's smc signatures
    DEX_METHODS = {
        DexPool.DEX_STON: {
            'method': 'get_pool_data',
            'expected': ['int', 'int', 'address', 'address', 'int', 'int', 'int', 'address', 'int', 'int']
        },
        DexPool.DEX_DEDUST: {
            'method': 'get_reserves',
            'expected': ['int', 'int']
        }
    }
    def __init__(self, tonapi: TonapiAdapter, executor: ContractsExecutor):
        CalculationBackend.__init__(self, "defillama backend for defi leaderboard",
                                    leaderboards=[SeasonConfig.DEFI])
        self.tonapi = tonapi
        self.executor = executor

    def get_update_time(self, config: SeasonConfig):
        # use the current time for now
        return int(time.time())

    """
    Returns pool TVL in USD for particular block (may be null, latest block in this case)
    """
    def get_pool_tvl(self, pool: DexPool, ton_rate: float, block=None):
        code, data = self.tonapi.get_state(pool.address, block)
        method_metadata = DefillamaDeFiBackend.DEX_METHODS[pool.dex]
        res = self.executor.execute(code, data, pool.address, method_metadata['method'], method_metadata['expected'])
        reserve0, reserve1 = int(res[0]), int(res[1])
        if pool.asset_position == DexPool.POSITION_LEFT:
            tvl = 2 * reserve0
        elif pool.asset_position == DexPool.POSITION_RIGHT:
            tvl = 2 * reserve1
        else:
            raise Exception(f"Unsupported asset position: {pool.asset_position}")
        if pool.asset_currency == DexPool.ASSET_USDT:
            tvl = tvl / 1e6
        elif pool.asset_currency == DexPool.ASSET_TON:
            tvl = tvl / 1e9 * ton_rate
        else:
            raise Exception(f"Unsupported asset: {pool.asset_currency}")
        return tvl

    def ton_rate(self, timestamp: int):
        TON = "ton:EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c"
        res = requests.get(f"https://coins.llama.fi/prices/historical/{timestamp}/{TON}?searchWidth=4h").json()
        return res['coins'][TON]['price']

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        # Start with estimated excluded TVL from boosted pools using on-chain data only
        current_ton_rate = self.ton_rate(min(int(time.time()), config.end_time))
        snapshot_ton_rate = self.ton_rate(config.start_time)
        logger.info(f"Snapshot TON rate: {snapshot_ton_rate}$, current TON rate: {current_ton_rate}$")

        assert config.block_before_start_ref is not None, "Start block is required for the DeFi leaderboard"

        end_block = None
        if int(time.time()) > config.end_time:
            end_block = config.block_before_end_ref
            assert end_block is not None, "Season is closed, one need to specify last block ref"
        logger.info(f"Getting TVL for {config.block_before_start_ref} and {end_block if end_block else 'latest block'}")

        excluded_snapshot = { DexPool.DEX_STON: 0, DexPool.DEX_DEDUST: 0}
        excluded_current = { DexPool.DEX_STON: 0, DexPool.DEX_DEDUST: 0}

        for pool in config.options[SeasonConfig.OPTION_DEFI_EXCLUDED_POOLS]:
            current_tvl = self.get_pool_tvl(pool, current_ton_rate, end_block)
            snapshot_tvl = self.get_pool_tvl(pool, snapshot_ton_rate, config.block_before_start_ref)
            logger.info(f"TVL for pool {pool.address} is {snapshot_tvl:0.2f}$ => {current_tvl:0.2f}$")
            excluded_snapshot[pool.dex] += snapshot_tvl
            excluded_current[pool.dex] += current_tvl

        logger.info(f"Total excluded current: {excluded_current}, snapshot: {excluded_snapshot}")

        def get_tvl_before(history, timestamp):
            *_, last_item = filter(lambda x: x['date'] < timestamp, history)
            return last_item['totalLiquidityUSD']

        logger.info("Running DeFiLlama backend for DeFi leaderboard")
        results: List[ProjectStat] = []
        for project in config.projects:
        
            res = requests.get(f'https://api.llama.fi/protocol/{project.defillama_slug}', headers={
                'User-Agent': 'TheOpenLeague',
                'Accept': '*/*'
            }).json()
            tvl_history = res['chainTvls']['TON']['tvl']
            snapshot_tvl = get_tvl_before(tvl_history, config.start_time)
            latest_tvl = get_tvl_before(tvl_history, config.end_time)
            correction_latest = -1 * excluded_current.get(project.name, 0)
            correction_snapshot = -1 * excluded_snapshot.get(project.name, 0)
            logger.info(f"{project.name}: {snapshot_tvl}({correction_snapshot}) => {latest_tvl}({correction_latest})")
            

            results.append(ProjectStat(
                name=project.name,
                metrics={
                    ProjectStat.DEFI_TVL_BEFORE: snapshot_tvl,
                    ProjectStat.DEFI_TVL_AFTER: latest_tvl,
                    ProjectStat.DEFI_TVL_BEFORE_COUNTED: snapshot_tvl + correction_snapshot,
                    ProjectStat.DEFI_TVL_AFTER_COUNTED: latest_tvl + correction_latest,
                    ProjectStat.DEFI_TVL_DELTA: latest_tvl - snapshot_tvl,
                    ProjectStat.DEFI_TVL_DELTA_COUNTED: latest_tvl + correction_latest - snapshot_tvl - correction_snapshot,
                    ProjectStat.URL: project.url,
                }
            ))


        return CalculationResults(ranking=results, build_time=1)
