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
    The largest value gets max (100%) and the lowest gets min (0%),
    all other values have result according to their rank in the set of values.
    Simple example: given values 1, 12, 2, 3, 4, 2, 3.
    Building ranks from it:
    #1: 12
    #2: 4
    #3: 3, 3
    #4: 2, 2
    #5: 1
    
    So #1 12 will get 100% (i.e 1, float value), #5 1 will get 0%,
    #2 4 - 75%, #3: 3, 3 - %50, #4: 2, 2 - %25        
    """
    def rank_index(self, p: ProjectStat, field: str, metrics):
        current = p.metrics[field]
        values = sorted(set(map(lambda x: x.metrics[field], metrics)), reverse=True)
        rank = len(values)
        for value in values:
            if value == current:
                break
            rank -= 1
        logger.info(f"Value : {current}, values: {values}, rank: {rank}, rank value: {1.0 * rank / len(values)}")
        return 1.0 * rank / len(values)

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
