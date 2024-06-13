from dataclasses import dataclass
from typing import List

from models.metric import Metric
from models.project_base import Project

@dataclass
class Token(Project):
    address: str # token address
    decimals: int # token decimals
    is_meme: bool = False # meme flag
    has_boost: bool = False


@dataclass
class App(Project):
    analytics_key: str # project name in tganalytics.xy
    metrics: List[Metric]

@dataclass
class NFT(Project):
    address: str # token address


@dataclass
class DeFi(Project):
    title: str # project title
    url: str # project url
    defillama_slug: str # Defillama slug