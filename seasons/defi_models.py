from typing import List

from models.results import ProjectStat
from models.scores import ScoreModel
from loguru import logger


"""
DeFi Leaderboard rewards calculator. Has two params - total_prize_pool and max_prize per project.
Each project gets reward in accordance with it TVL impact, projects with negative TVL impact
have no rewards
"""
class DeFiWeightedRewards(ScoreModel):

    def __init__(self, total_prize_pool, max_prize):
        super().__init__()
        self.total_prize_pool = total_prize_pool
        self.max_prize = max_prize


    def calculate(self, metrics: List[ProjectStat]):
        total_tvl_delta = 0
        for project in metrics:
            delta = project.metrics[ProjectStat.DEFI_TVL_DELTA_COUNTED]
            if delta > 0 and project.metrics[ProjectStat.PRIZES]:
                total_tvl_delta += delta
        logger.info(f"Total positive TVL delta is {total_tvl_delta:0.2f}$")

        prize_pool = self.total_prize_pool
        counted_tvl = 0
        for project in sorted(metrics, key=lambda m: m.metrics[ProjectStat.DEFI_TVL_DELTA_COUNTED], reverse=True):
            delta = project.metrics[ProjectStat.DEFI_TVL_DELTA_COUNTED]
            if total_tvl_delta <=0 or delta < 0 or not project.metrics[ProjectStat.PRIZES]:
                reward = 0
            else:
                reward = min(prize_pool * delta / (total_tvl_delta - counted_tvl), self.max_prize)
                counted_tvl += delta
                prize_pool -= reward
                logger.info(f"Reward for {project.name} is {reward}, counted tvl is {counted_tvl}, "
                            f"prize pool is {prize_pool}")
            logger.info(f"Calculating score for {project}")
            project.score = reward
            project.metrics[ProjectStat.REWARD] = reward

        return sorted(metrics, key=lambda m: m.score, reverse=True)
