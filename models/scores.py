"""
Scores models
"""
from typing import List

from models.results import ProjectStat


"""
Simple scoring model. Accepts list of the projects with metrics and returns the same list
with calculated scores
"""
class ScoreModel:
    def calculate(self, metrics: List[ProjectStat]):
        raise NotImplemented()
