"""
Scores models
"""
from typing import List

from models.results import ProjectStat
from loguru import logger


"""
Simple scoring model. Accepts list of the projects with metrics and returns the same list
with calculated scores
"""
class ScoreModel:
    """
    What min value (in TON equivalent) is required for user to be treated as a new holder
    """
    PARAM_TOKEN_MIN_VALUE_FOR_NEW_HOLDER = "token_min_value_for_new_holder"

    def __init__(self):
        self.params = {}

    def param(self, key):
        return self.params[key]

    def get_max(self, field: str, metrics):
        return max(map(lambda x: x.metrics[field], metrics))

    def get_min(self, field: str, metrics):
        return min(map(lambda x: x.metrics[field], metrics))

    """
    Normalize value on the max value in the data set
    """
    def normalized_max(self, p: ProjectStat, field: str, metrics):
        return p.metrics[field] / self.get_max(field, metrics)

    """
    Normalize value based on the min and max values. So min value will be 0 and
    max value will be 1
    """
    def normalized_min_max(self, p: ProjectStat, field: str, metrics):
        max_ = self.get_max(field, metrics)
        min_ = self.get_min(field, metrics)
        if max_ == min_:
            logger.error(f"Max = min for {field}")
            return 0
        return (p.metrics[field] - min_) / (max_ - min_)

    def calculate(self, metrics: List[ProjectStat]):
        raise NotImplemented()
