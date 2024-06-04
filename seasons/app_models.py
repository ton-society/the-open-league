from typing import List

from models.results import ProjectStat
from models.scores import ScoreModel
from loguru import logger


"""
App leaderboard score model, launched since S4
40% - UAW
20% - Median TX count per user
5%  - non-premium off-chain
15%  - premium off-chain
20% - Stickiness Factor (off-chain) (avg.DAU / Season Active Users)
"""
class AppLeaderboardModelV2(ScoreModel):
    def calculate(self, metrics: List[ProjectStat]):
        def get_max(field: str):
            return max(map(lambda x: x.metrics[field], metrics))

        def normalized_max(p: ProjectStat, field: str):
            return p.metrics[field] / get_max(field)

        for project in metrics:
            logger.info(f"Calculating score for {project}")
            project.score = 40 * normalized_max(project, ProjectStat.APP_ONCHAIN_UAW) + \
                    20 * normalized_max(project, ProjectStat.APP_ONCHAIN_MEDIAN_TX) + \
                    5 * normalized_max(project, ProjectStat.APP_OFFCHAIN_NON_PREMIUM_USERS) + \
                    15 * normalized_max(project, ProjectStat.APP_OFFCHAIN_PREMIUM_USERS) + \
                    20 * normalized_max(project, ProjectStat.APP_STICKINESS)
        return project