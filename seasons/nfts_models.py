from typing import List

from models.results import ProjectStat
from models.scores import ScoreModel
from loguru import logger

"""
TODO
"""
class NFTLeaderboardModelV1(ScoreModel):
    def __init__(self):
        super().__init__()

    def calculate(self, metrics: List[ProjectStat]):
        for project in metrics:
            logger.info(f"Calculating score for {project}")
            project.score = self.normalized_max(project, ProjectStat.NFT_VOLUME, metrics)

        return sorted(metrics, key=lambda m: m.score, reverse=True)
