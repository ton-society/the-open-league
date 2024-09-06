from dataclasses import dataclass, field
from typing import List, Dict

from models.project_base import Project
from models.scores import ScoreModel

@dataclass
class DexPool:
    DEX_STON = 'Ston.fi'
    DEX_DEDUST = 'DeDust'
    ASSET_USDT = 'usdt'
    ASSET_TON = 'ton'
    POSITION_LEFT = 0
    POSITION_RIGHT = 1

    address: str # pool address in friendly format
    dex: str # one of DEX_STON or DEX_DEDUST
    asset_position: int # asset position inside the pool (0 or 1, or even better POSITION_LEFT or POSITION_RIGHT)
    asset_currency: int # ASSET_USDT if pool contains USDT or ASSET_TON if only ton


@dataclass
class SeasonConfig:
    APPS = "apps" # applications leaderboard
    TOKENS = "tokens" # tokens leaderboard
    NFTS = "nfts" # NFTs leaderboard
    DEFI = "defi" # TVL leaderboard

    OPTION_DEFI_EXCLUDED_POOLS = "excluded_pools"

    leaderboard: str # leaderboard name
    name: str # season name
    start_time: int # start time in unixtime
    end_time: int # start time in unixtime


    projects: List[Project]
    # backend_config: Dict[str, Dict[str, str]] # backend specific configs

    score_model: ScoreModel # score model

    options: Dict = field(default_factory=dict) # custom options

    """
    Block refs are optional, but it is required for some leaderboards (for instance DeFi). 
    Block refs must be passed in the format  (workchain,shard,seqno,root_hash,file_hash), 
    where root_hash and file_hash are hex values in upper case, for example:
    1,8000000000000000,4234234,3E575DAB1D25
    """
    block_before_start_ref: str = None # ref for the last block exactly before the start_time
    block_before_end_ref: str = None # ref for the last block of the season (i.e. before end_time)


    """
    Address of SBT collection which is used for enrollment
    """
    enrollment_sbt: str = None 
    # for SQL usage
    def safe_season_name(self):
        return self.name.replace(".", '_')