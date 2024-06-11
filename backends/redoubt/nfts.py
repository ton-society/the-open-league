from typing import Dict

from models.backend import CalculationBackend
from models.backends import BACKEND_REDOUBT
from models.metric import MetricImpl, CalculationContext
from models.results import ProjectStat, CalculationResults
from models.season_config import SeasonConfig
import psycopg2
import psycopg2.extras
from loguru import logger

class RedoubtNFTsBackend(CalculationBackend):
    def __init__(self):
        CalculationBackend.__init__(self, "re:doubt backend for NFTs leaderboard",
                                    leaderboards=[SeasonConfig.NFTS])

    """
    Update time for auxiliary table with messages
    """
    def get_update_time(self, config: SeasonConfig):
        with psycopg2.connect() as pg:
            with pg.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(f"""
                -- TODO
                """)
                return cursor.fetchone()['last_time']

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        logger.info("Running re:doubt backend for NFTs leaderboard SQL generation")
        
        context = CalculationContext(season=config, impl=BACKEND_REDOUBT)
        
        for project in config.projects:
            pass
        SQL = f"""
        -- TODO
        """
        logger.info(f"Generated SQL: {SQL}")

        results: Dict[str, ProjectStat] = {}
        with psycopg2.connect() as pg:
            if dry_run:
                logger.info("Running SQL query in dry_run mode")
                with pg.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                    cursor.execute(f"explain {SQL}")
            else:
                logger.info("Running SQL query in production mode")
                with pg.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                    cursor.execute(SQL)
                    for row in cursor.fetchall():
                        logger.info(row)
                        assert row['project'] not in results
                        results[row['project']] = ProjectStat(
                            name=row['project'],
                            metrics={}
                        )
                        # TODO
                        # results[row['project']].metrics[ProjectStat.NFT_???] = int(row['???'])
                logger.info("NFT query finished")
        return CalculationResults(ranking=results.values(), build_time=1)

