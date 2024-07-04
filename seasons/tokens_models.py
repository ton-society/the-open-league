from typing import List

from models.results import ProjectStat
from models.scores import ScoreModel
from loguru import logger


"""
Token leaderboard score model, launched since S4
30% - TVL Delta
40% - New holders
30% - Price change (normalised on sqrt(TVL))
"""
class TokenLeaderboardModelV4(ScoreModel):


    def __init__(self):
        super().__init__()
        self.params[ScoreModel.PARAM_TOKEN_MIN_VALUE_FOR_NEW_HOLDER] = 1.0 # 1 TON

    def calculate(self, metrics: List[ProjectStat]):
        for project in metrics:
            logger.info(f"Calculating score for {project}")
            project.score = 40 * self.normalized_max(project, ProjectStat.TOKEN_NEW_USERS_WITH_MIN_AMOUNT, metrics) + \
                            30 * self.normalized_min_max(project, ProjectStat.TOKEN_TVL_CHANGE, metrics) + \
                            30 * self.normalized_min_max(project, ProjectStat.TOKEN_PRICE_CHANGE_NORMED, metrics)

        return sorted(metrics, key=lambda m: m.score, reverse=True)


"""
Token leaderboard score model, launched since S5. The only metrics is price change
"""
class TokenLeaderboardModelV5(ScoreModel):
    def __init__(self):
        super().__init__()
        self.params[ScoreModel.PARAM_TOKEN_MIN_VALUE_FOR_NEW_HOLDER] = 1.0 # 1 TON

    def calculate(self, metrics: List[ProjectStat]):
        for project in metrics:
            logger.info(f"Calculating score for {project}")
            project.score = project.metrics[ProjectStat.TOKEN_TVL_CHANGE]

        return sorted(metrics, key=lambda m: m.score, reverse=True)
