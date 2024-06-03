from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ProjectStat:
    name: str
    score: float
    metrics: Dict[str, float]

@dataclass
class CalculationResults:
    ranking: List[ProjectStat]

