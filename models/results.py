from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ProjectStat:
    APP_OFFCHAIN_NON_PREMIUM_USERS = 'offchain_non_premium_users'
    APP_OFFCHAIN_PREMIUM_USERS = 'offchain_premium_users'
    APP_OFFCHAIN_AVG_DAU = 'offchain_avg_dau'
    APP_OFFCHAIN_TOTAL_USERS = 'offchain_total_unique_users'
    APP_STICKINESS = 'offchain_stickiness'

    APP_ONCHAIN_TOTAL_TX = 'onchain_total_tx'
    APP_ONCHAIN_UAW = 'onchain_uaw'
    APP_ONCHAIN_MEDIAN_TX = 'onchain_median_tx'

    TOKEN_TVL_CHANGE = 'token_tvl_change'
    TOKEN_START_TVL = 'token_start_tvl'
    TOKEN_LAST_TVL = 'token_last_tvl'
    TOKEN_PRICE_BEFORE = 'token_price_before'
    TOKEN_PRICE_AFTER = 'token_price_after'
    TOKEN_PRICE_CHANGE_NORMED = 'price_change_normed'
    TOKEN_PRICE_CHANGE_SIMPLE = 'price_change_simple'
    TOKEN_NEW_USERS_WITH_MIN_AMOUNT = 'new_users_min_amount'
    TOKEN_ADDRESS = 'token_address'
    TOKEN_IS_MEME = 'is_meme'
    TOKEN_HAS_BOOST = 'has_boost'

    NFT_VOLUME = 'volume'

    DEFI_TVL_BEFORE = 'defi_tvl_before'
    DEFI_TVL_AFTER = 'defi_tvl_after'
    DEFI_TVL_DELTA = 'defi_tvl_delta'

    TITLE = 'title'
    URL = 'url'


    name: str
    metrics: Dict[str, float]
    score: float = None

@dataclass
class CalculationResults:
    ranking: List[ProjectStat]
    build_time: int

