import time
from typing import Dict

from models.backend import CalculationBackend
from models.backends import BACKEND_REDOUBT
from models.metric import MetricImpl, CalculationContext
from models.results import ProjectStat, CalculationResults
from models.scores import ScoreModel
from models.season_config import SeasonConfig
import psycopg2
import json
import psycopg2.extras
from loguru import logger

"""
This backend will be used to aggegate score points for all users into project metrics
"""

class ToncenterCppAppsScores2Projects(CalculationBackend):
    def __init__(self, connection):
        CalculationBackend.__init__(self, "toncenter cpp indexer backend for App leaderboard, project version",
                                    leaderboards=[SeasonConfig.APPS])
        self.connection = connection

    """
    Update time for auxiliary table with messages
    """
    def get_update_time(self, config: SeasonConfig):
        return 1726138800

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):

        logger.info("Running toncenter backend for App leaderboard SQL generation, projects version")
        PROJECTS_NAMES = []
        context = CalculationContext(season=config, impl=BACKEND_REDOUBT)
        
        for project in config.projects:
            PROJECTS_NAMES.append(f"""
            select '{project.name}' as project, '{project.url}' as url
            """)
        PROJECTS_NAMES = "\n union all \n".join(PROJECTS_NAMES)
        
        SQL = f"""
        with project_names as (
        {PROJECTS_NAMES}
        ), eligible as (
          select address, 1 as eligible from tol.apps_users_stats_{config.safe_season_name()} auss
          join tol.enrollment_{config.safe_season_name()} es using(address)
    group by address having count(1) > 1
        )
        select project, url, count(distinct address) as total_uaw, coalesce(sum(eligible), 0) as enrolled_wallets,
        coalesce(cast(sum(points) / sum(eligible) as int), 0) as average_score, coalesce(sum(points), 0) as total_points
        from project_names 
        left join tol.apps_users_stats_{config.safe_season_name()} using(project)
        left join eligible using(address)
        left join tol.apps_points_{config.safe_season_name()} using(address)
        group by 1, 2
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
                    results[row['project']] = ProjectStat(
                        name=row['project'],
                        metrics={
                            ProjectStat.URL: row['url'],
                            ProjectStat.APP_ONCHAIN_UAW: row['total_uaw'],
                            ProjectStat.APP_ONCHAIN_ENROLLED_UAW: row['enrolled_wallets'],
                            ProjectStat.APP_AVERAGE_SCORE: row['average_score'],
                            ProjectStat.APP_TOTAL_POINTS: row['total_points']
                        }
                    )

            self.connection.commit()
            logger.info("Main query finished")
            
        return CalculationResults(ranking=results.values(), build_time=1)

