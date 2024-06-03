from models.backend import CalculationBackend
from models.backends import BACKEND_TONALYTICA
from models.metric import MetricImpl, CalculationContext
from models.season_config import SeasonConfig
from loguru import logger

class TonalyticaAppBackend(CalculationBackend):
    def __init__(self):
        CalculationBackend.__init__(self, "Tonalytica App leaderboard",
                                    leaderboards=[SeasonConfig.APPS])

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        logger.info("Running tonalytica App leaderboard SQL generation")
        PROJECTS = []
        PROJECTS_ALIASES = []
        context = CalculationContext(season=config, impl=BACKEND_TONALYTICA)
        
        for project in config.projects:
            context.project = project
            metrics = []
            for metric in project.metrics:
                metrics.append(metric.calculate(context))
            metrics = "\nUNION ALL\n".join(metrics)
            PROJECTS.append(f"""
            project_{project.name} as (
            {metrics}
            )
            """)
            PROJECTS_ALIASES.append("""
            select * from project_{project.name}
            """)
        PROJECTS = ",\n".join(PROJECTS)
        PROJECTS_ALIASES = "\nUNION ALL\n".join(PROJECTS_ALIASES)
        SQL = f"""
        with messages_local as (
            select * from tol.messages_{config.name}
        ),
        {PROJECTS},
        all_projects as (
        {PROJECTS_ALIASES}        
        )
        select * from all_projects
        """
        logger.info(f"Generated SQL: {SQL}")

    def _generate_project_block(self, config: SeasonConfig, metric: MetricImpl):
        return metric.calculate(config)
