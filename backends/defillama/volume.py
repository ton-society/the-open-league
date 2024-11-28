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
from datetime import datetime
from loguru import logger

"""
DeFi leaderboard based on the volume data reported to DeFiLlama 
"""
class DefillamaDeFiVolumeBackend(CalculationBackend):
    def __init__(self):
        CalculationBackend.__init__(self, "defillama backend for defi leaderboard (Volume)",
                                    leaderboards=[SeasonConfig.DEFI])

    def get_update_time(self, config: SeasonConfig):
        # use the current time for now
        return int(time.time())

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        logger.info("Running DeFiLlama backend for DeFi leaderboard (Volume)")
        results: List[ProjectStat] = []
        DAY = 86400
        for project in config.projects:
            if time.time() - config.start_time < DAY:
                sum_volume = 0
            else:
                res = requests.get(f'https://api.llama.fi/summary/{project.category}/{project.defillama_slug}', headers={
                    'User-Agent': 'TheOpenLeague',
                    'Accept': '*/*'
                }).json()
                sum_volume = 0
                """
                Defillama returns data points aggregated by UTC days, but the season has boundaries at 11 UTC.
                Se we should approximate partial days using linear interpolation.
                """
                def in_season(ts):
                    return ts >= config.start_time and ts < config.end_time
                for item in res['totalDataChartBreakdown']:
                    ts = item[0]
                    daily_volume = sum(item[1]['ton'].values())
                    # logger.info(item)
                    if in_season(ts) and in_season(ts + DAY):
                        sum_volume += daily_volume
                        logger.info(f"Adding full day for {ts}")
                    elif not in_season(ts) and in_season(ts + DAY):
                        # partial first day
                        share = 1.0 * (config.start_time - ts) / DAY
                        sum_volume += daily_volume * share
                        logger.info(f"Adding partial firstday for {ts} with share {share}")
                    elif not in_season(ts + DAY) and in_season(ts):
                        # partial last day
                        share = 1.0 * (ts - config.end_time) / DAY
                        sum_volume += daily_volume * share
                        logger.info(f"Adding partial last day for {ts} with share {share}")

                
            logger.info(f"Total volume for {project.name}: {sum_volume}$")

            results.append(ProjectStat(
                name=project.name,
                metrics={
                    ProjectStat.DEFI_VOLUME_USD: sum_volume,
                    ProjectStat.URL: project.url,
                }
            ))


        return CalculationResults(ranking=results, build_time=1)
