from typing import List, Optional

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
Token leaderboard score model, launched since S5
30% - base TVL Delta weight
40% - base New holders weight
30% - base Price change (normalised on sqrt(TVL)) weight
"""
class TokenLeaderboardModelV5(ScoreModel):
    def __init__(self, reward_list: Optional[List[int]] = None):
        super().__init__()
        self.params[ScoreModel.PARAM_TOKEN_MIN_VALUE_FOR_NEW_HOLDER] = 1.0 # 1 TON
        self.reward_list = reward_list
        self.tvl_category = {
            "$10M - $20M": {"low": 10_000_000, "high": None, "coefficient": 1},
            "$5M - $10M": {"low": 5_000_000, "high": 10_000_000, "coefficient": 0.8},
            "$2M - $5M": {"low": 2_000_000, "high": 5_000_000, "coefficient": 0.6},
            "$1M - $2M": {"low": 1_000_000, "high": 2_000_000, "coefficient": 0.5},
            "$0.5M - $1M": {"low": 500_000, "high": 1_000_000, "coefficient": 0.4},
            "$0.1M - $0.5M": {"low": None, "high": 500_000, "coefficient": 0.3},
        }
        self.ton_usd_rate = 7.50648

    def get_tvl_category(self, tvl_value) -> str:
        for category_name, limits in self.tvl_category.items():
            if (not limits["low"] or tvl_value > limits["low"]) and (not limits["high"] or tvl_value <= limits["high"]):
                return category_name

    def calculate(self, metrics: List[ProjectStat]):
        for project in metrics:
            logger.info(f"Calculating score for {project}")
            start_tvl_usd = project.metrics[ProjectStat.TOKEN_START_TVL] * self.ton_usd_rate
            project.metrics[ProjectStat.TOKEN_TVL_CATEGORY] = self.get_tvl_category(start_tvl_usd)
            price_change_weight = 30 * self.tvl_category[project.metrics[ProjectStat.TOKEN_TVL_CATEGORY]]["coefficient"]
            tvl_change_weight = 30 + (30 - price_change_weight) * 3 / 7
            new_holders_weight = 40 + (30 - price_change_weight) * 4 / 7
            project.score = new_holders_weight * self.normalized_max(project, ProjectStat.TOKEN_NEW_USERS_WITH_MIN_AMOUNT, metrics) + \
                            tvl_change_weight * self.normalized_min_max(project, ProjectStat.TOKEN_TVL_CHANGE, metrics) + \
                            price_change_weight * self.normalized_min_max(project, ProjectStat.TOKEN_PRICE_CHANGE_NORMED, metrics)

        return self.calculate_rewards(sorted(metrics, key=lambda m: m.score, reverse=True))
