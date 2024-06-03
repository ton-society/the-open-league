from dataclasses import dataclass
from typing import List, Dict

from models.project_base import Project


@dataclass
class SeasonConfig:
    APPS = "apps" # applications leaderboard
    TOKENS = "tokens" # tokens leaderboard

    leaderboard: str # leaderboard name
    name: str # season name
    start_time: int # start time in unixtime
    end_time: int # start time in unixtime

    projects: List[Project]
    # backend_config: Dict[str, Dict[str, str]] # backend specific configs