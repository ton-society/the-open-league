from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ProjectStat:
    name: str
    metrics: Dict[str, float]
    score: float = None

@dataclass
class CalculationResults:
    ranking: List[ProjectStat]
    build_time: int

