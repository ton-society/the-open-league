from dataclasses import dataclass
from typing import List

from models.metric import Metric
from models.project_base import Project

@dataclass
class Token(Project):
    address: str # token address

@dataclass
class App(Project):
    analytics_key: str # project name in tganalytics.xy
    metrics: List[Metric]