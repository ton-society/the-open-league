from dataclasses import dataclass
from typing import List
from loguru import logger
from tonsdk.utils import Address

from models.backends import BACKEND_REDOUBT, BACKEND_TONCENTER_CPP
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
implementation based on re:doubt backend (https://github.com/re-doubt/ton-indexer)
"""
class RedoubtMetricImpl(MetricImpl):
    def name(self):
        return BACKEND_REDOUBT

"""
implementation based on toncenter-cpp backend (https://github.com/toncenter/ton-index-worker)
"""
class ToncenterCppMetricImpl(MetricImpl):
    def name(self):
        return BACKEND_TONCENTER_CPP
    
    def to_raw(self, address: str):
        return Address(address).to_string(False).upper()

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
        logger.error(f"Unable to find metric implementation {context.impl} for {self.__class__.__name__}")
        raise Exception(f"{context.impl} implementation not found")