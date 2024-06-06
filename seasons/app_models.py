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
        for project in metrics:
            logger.info(f"Calculating score for {project}")
            project.score = 40 * self.normalized_max(project, ProjectStat.APP_ONCHAIN_UAW, metrics) + \
                    20 * self.normalized_max(project, ProjectStat.APP_ONCHAIN_MEDIAN_TX, metrics) + \
                    5 * self.normalized_max(project, ProjectStat.APP_OFFCHAIN_NON_PREMIUM_USERS, metrics) + \
                    15 * self.normalized_max(project, ProjectStat.APP_OFFCHAIN_PREMIUM_USERS, metrics) + \
                    20 * self.normalized_max(project, ProjectStat.APP_STICKINESS, metrics)

        return sorted(metrics, key=lambda m: m.score, reverse=True)
