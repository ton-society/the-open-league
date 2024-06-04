from typing import List

from models.results import ProjectStat
from models.scores import ScoreModel
from loguru import logger


"""
App leaderboard score model, launched since S4
40% - UAW
30% - Number of tx  TODO - migrate to median tx per user
5%  - non-premium off-chain
5%  - premium off-chain
20% - Stickiness Factor (off-chain)
"""
class AppLeaderboardModelV2(ScoreModel):
    def calculate(self, metrics: List[ProjectStat]):
        def get_max(field: str):
            return max(map(lambda x: x.metrics[field], metrics))

        def normalized_max(p: ProjectStat, field: str):
            return p.metrics[field] / get_max(field)

        for project in metrics:
            logger.info(f"Calculating score for {project}")
            project.score = 40 * normalized_max(project, 'total_users') + \
                    30 * normalized_max(project, 'tx_count') + \
                    5 * normalized_max(project, 'non_premium_users') + \
                    5 * normalized_max(project, 'premium_users')
        return project