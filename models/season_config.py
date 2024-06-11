from dataclasses import dataclass
from typing import List, Dict

from models.project_base import Project
from models.scores import ScoreModel


@dataclass
class SeasonConfig:
    APPS = "apps" # applications leaderboard
    TOKENS = "tokens" # tokens leaderboard
    NFTS = "nfts" # NFTs leaderboard

    leaderboard: str # leaderboard name
    name: str # season name
    start_time: int # start time in unixtime
    end_time: int # start time in unixtime

    projects: List[Project]
    # backend_config: Dict[str, Dict[str, str]] # backend specific configs

    score_model: ScoreModel # score model

    # for SQL usage
    def safe_season_name(self):
        return self.name.replace(".", '_')