import time
from typing import Dict

from models.backend import CalculationBackend
from models.backends import BACKEND_REDOUBT
from models.metric import MetricImpl, CalculationContext
from models.results import ProjectStat, CalculationResults
from models.scores import ScoreModel
from models.season_config import SeasonConfig
import psycopg2
import psycopg2.extras
from loguru import logger

class RedoubtTokensBackend(CalculationBackend):
    def __init__(self, connection):
        CalculationBackend.__init__(self, "re:doubt backend for Tokens leaderboard",
                                    leaderboards=[SeasonConfig.TOKENS])
        self.connection = connection

    def get_update_time(self, config: SeasonConfig):
        with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute("""
            select extract('epoch' from update_time) as update_time  from chartingview.token_agg_price tap order by update_time desc limit 1
            """)
            return cursor.fetchone()['update_time']

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        logger.info("Running re:doubt backend for Token leaderboard SQL generation")
        PROJECTS = []
        # context = CalculationContext(season=config, impl=BACKEND_REDOUBT)
        for project in config.projects:
            PROJECTS.append(f"""
            select '{project.name}' as symbol, '{project.address}' as address, {project.decimals} as decimals,
            {project.is_meme} as is_meme, {project.prizes} as prizes, {project.has_boost} as has_boost, '{project.url if project.url else ""}' as url,
            '{project.boost_link if project.boost_link else ""}' as boost_link
            """)
        PROJECTS = "\nunion all\n".join(PROJECTS)

        balances_table = "mview_jetton_balances"
        if (time.time()) > config.end_time:
            balances_table = f"tol.token_balances_snapshot_{config.safe_season_name()}"
        SQL = f"""
            with tol_tokens as (
                {PROJECTS}                
            ), tol_ton_or_stable as (
            -- allowed tokens for pairs - TON or stable or LSDs
                select 'EQBPAVa6fjMigxsnHF33UQ3auufVrg2Z8lBZTY9R-isfjIFr' as address union all
                select 'EQDQoc5M3Bh8eWFephi9bClhevelbZZvWhkqdo80XuY_0qXv' as address union all
                select 'EQCM3B12QK1e4yZSf8GtBRT0aLMNyEsBc_DhVfRRtOEffLez' as address union all
                select 'EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c' as address union all
                select 'EQCajaUU1XXSAjTD-xOV7pE49fGtg4q8kF3ELCOJtGvQFQ2C' as address union all
                select 'EQB-MPwrd1G6WKNkLz_VnV6WqBDd142KMQv-g1O-8QUA3728' as address union all
                select 'EQBynBO23ywHy_CgarY9NK9FTz0yDsG82PtcbSTQgGoXwiuA' as address union all
                select 'EQC_1YoM8RBixN95lz7odcF3Vrkc_N8Ne7gQi7Abtlet_Efi' as address union all
                select 'EQC61IQRl0_la95t27xhIpjxZt32vl1QQVF2UgTNuvD18W-4' as address union all
                select 'EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs' as address union all
                select 'EQDNhy-nxYFgUqzfUzImBEP67JqsyMIcyk2S5_RwNNEYku0k' as address union all
                select 'EQC98_qAmNEptUtPc7W6xdHh_ZHrBUFpw5Ft_IzNU20QAJav' as address union all
                select 'EQDPdq8xjAhytYqfGSX8KcFWIReCufsB9Wdg0pLlYSO_h76w' as address 
            ),
            latest_balances as (
                select * from {balances_table}
            ), pools as (
              -- all DEX pools for our tokens
              select distinct tol_tokens.symbol, tol_tokens.address, thd.address as pool
              from tvl_history_datamart thd join tol_tokens on tol_tokens.address = thd.jetton_a
              where jetton_b in (select address from tol_ton_or_stable)
              and build_time >=  to_timestamp({config.start_time}) - interval '7 day'
              union
              select distinct tol_tokens.symbol, tol_tokens.address, thd.address as pool
              from tvl_history_datamart thd join tol_tokens on tol_tokens.address = thd.jetton_b
              where jetton_a in (select address from tol_ton_or_stable)
              and build_time >=  to_timestamp({config.start_time}) - interval '7 day'
            ), tvl_prior_start_all as (
              -- TVL for 14 days before the start
              select distinct on(thd.address ) build_time, p.symbol, tvl_ton
              from tvl_history_datamart thd join pools p on thd.address = p.pool
              and build_time >=  to_timestamp({config.start_time}) - interval '20 day' -- just for performance
              and build_time <  to_timestamp({config.start_time}) - interval '14 day' -- end of the S4 season
              order by thd.address, build_time desc
            ), tvl_prior_start as (
              select symbol, sum(tvl_ton) as start_tvl,
              (
                select rate from ton_usd_rates 
                where build_time < to_timestamp({config.start_time}) - interval '14 day' 
                order by build_time desc limit 1
              ) * sum(tvl_ton) as start_tvl_usd
              from tvl_prior_start_all
              group by 1
            ), current_tvl as (
              -- TVL during the season
              select distinct on(thd.address ) build_time, p.symbol, tvl_ton
              from tvl_history_datamart thd join pools p on thd.address = p.pool
              and build_time >=  to_timestamp({config.start_time})
              and build_time <  to_timestamp({config.end_time})
              order by thd.address, build_time desc
            ), last_tvl as (
              -- latest values
              select symbol, sum(tvl_ton) as tvl from current_tvl
              group by 1
            )
            , price_snapshots as (
              -- price value before the start  and at the end
              select symbol, (
                select price_ton from chartingview.token_agg_price_history ph where ph.address = tt.address
                and build_time < to_timestamp({config.start_time} ) order by build_time desc limit 1
              ) as price_before, (
                select price_ton from chartingview.token_agg_price_history ph where ph.address = tt.address
                and build_time <= to_timestamp({config.end_time} ) order by build_time desc limit 1
              )  as price_after from tol_tokens tt
            ), price_delta as (
              select symbol, price_before, price_after, case
                when price_before is null then 0
                else (price_after - price_before) / (price_before)
              end as price_change
              from price_snapshots
            )
            select tol_tokens.symbol,
            tol_tokens.address,
            is_meme,
            has_boost,
            prizes,
            url, boost_link,
            coalesce(start_tvl, 0) as start_tvl,
            coalesce(start_tvl_usd, 0) as start_tvl_usd,
            coalesce(last_tvl.tvl, 0) as last_tvl,
            coalesce(100 * coalesce(price_change, 0), 0) as price_delta,
            coalesce(price_before, 0) as price_before,
            coalesce(price_after, 0) as price_after
            from tol_tokens 
            left join last_tvl on last_tvl.symbol = tol_tokens.symbol
            left join tvl_prior_start on tvl_prior_start.symbol = tol_tokens.symbol
            left join price_delta on price_delta.symbol = tol_tokens.symbol
        """
        logger.info(f"Generated SQL: {SQL}")

        results: Dict[str, ProjectStat] = {}
        if dry_run:
            logger.info("Running SQL query in dry_run mode")
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(f"explain {SQL}")
        else:
            logger.info("Running SQL query in production mode")
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(SQL)
                for row in cursor.fetchall():
                    logger.info(row)
                    assert row['symbol'] not in results
                    results[row['symbol']] = ProjectStat(
                        name=row['symbol'],
                        metrics={}
                    )
                    results[row['symbol']].metrics[ProjectStat.TOKEN_ADDRESS] = row['address']
                    results[row['symbol']].metrics[ProjectStat.PRIZES] = row['prizes']
                    results[row['symbol']].metrics[ProjectStat.REWARD] = 0
                    results[row['symbol']].metrics[ProjectStat.TOKEN_IS_MEME] = row['is_meme']
                    results[row['symbol']].metrics[ProjectStat.TOKEN_HAS_BOOST] = row['has_boost']
                    results[row['symbol']].metrics[ProjectStat.TOKEN_START_TVL] = int(row['start_tvl'])
                    results[row['symbol']].metrics[ProjectStat.TOKEN_START_TVL_USD] = int(row['start_tvl_usd'])
                    results[row['symbol']].metrics[ProjectStat.TOKEN_LAST_TVL] = int(row['last_tvl'])
                    results[row['symbol']].metrics[ProjectStat.TOKEN_PRICE_BEFORE] = float(row['price_before'])
                    results[row['symbol']].metrics[ProjectStat.TOKEN_PRICE_AFTER] = float(row['price_after'])
                    results[row['symbol']].metrics[ProjectStat.TOKEN_PRICE_CHANGE_SIMPLE] = float(row['price_delta'])
                    results[row['symbol']].metrics[ProjectStat.URL] = row['url']
                    results[row['symbol']].metrics[ProjectStat.TOKEN_BOOST_LINK] = row['boost_link']
            logger.info("Tokens query finished")

        return CalculationResults(ranking=results.values(), build_time=1)  # TODO build time
