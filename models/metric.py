from dataclasses import dataclass
from typing import List
from loguru import logger

from models.backends import BACKEND_TONALYTICA
from models.project_base import Project
from models.season_config import SeasonConfig


@dataclass
class CalculationContext:
    season: SeasonConfig # season config
    impl: str # implementation name
    project: Project = None

"""
Specific metric implementation
"""
class MetricImpl:
    def name(self):
        raise NotImplemented()

    def calculate(self, context: CalculationContext, metric):
        raise NotImplemented()

"""
Tonalytica implementation
"""
class TonalyticaMetricImpl(MetricImpl):
    def name(self):
        return BACKEND_TONALYTICA


"""
Metric base class. Encapsulates implementations. 
"""
class Metric:
    def __init__(self, description, implementations):
        self.description = description
        self.implementations: List[MetricImpl] = implementations

    """
    Main entry point for calculation.
    """
    def calculate(self, context: CalculationContext):
        for impl in self.implementations:
            if impl.name() == context.impl:
                return impl.calculate(context, self)
        logger.error(f"Unable to find metric implementation {context.impl}")
        raise Exception(f"{context.impl} implementation not found")