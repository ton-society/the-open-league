from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ProjectStat:
    PRIZES = 'prizes'
    REWARD = 'reward'
    POSSIBLE_REWARD = 'possible_reward'

    APP_OFFCHAIN_NON_PREMIUM_USERS = 'offchain_non_premium_users'
    APP_OFFCHAIN_PREMIUM_USERS = 'offchain_premium_users'
    APP_OFFCHAIN_AVG_DAU = 'offchain_avg_dau'
    APP_OFFCHAIN_TOTAL_USERS = 'offchain_total_unique_users'
    APP_STICKINESS = 'offchain_stickiness'

    APP_ONCHAIN_TOTAL_TX = 'onchain_total_tx'
    APP_ONCHAIN_UAW = 'onchain_uaw'
    APP_ONCHAIN_ENROLLED_UAW = 'onchain_enrolled_uaw'
    APP_AVERAGE_SCORE = 'average_score'
    APP_ONCHAIN_MEDIAN_TX = 'onchain_median_tx'

    TOKEN_TVL_CATEGORY = 'token_tvl_category'
    TOKEN_TVL_CHANGE = 'token_tvl_change'
    TOKEN_START_TVL = 'token_start_tvl'
    TOKEN_TVL_CATEGORY_VALUE = 'token_tvl_category_value'
    TOKEN_START_TVL_USD = 'token_start_tvl_usd'
    TOKEN_LAST_TVL = 'token_last_tvl'
    TOKEN_PRICE_BEFORE = 'token_price_before'
    TOKEN_PRICE_AFTER = 'token_price_after'
    TOKEN_PRICE_CHANGE_NORMED = 'price_change_normed'
    TOKEN_PRICE_CHANGE_SIMPLE = 'price_change_simple'
    TOKEN_NEW_USERS_WITH_MIN_AMOUNT = 'new_users_min_amount'
    TOKEN_ADDRESS = 'token_address'
    TOKEN_IS_MEME = 'is_meme'
    TOKEN_HAS_BOOST = 'has_boost'
    TOKEN_BOOST_LINK = 'boost_link'

    NFT_VOLUME = 'volume'

    DEFI_TVL_BEFORE = 'defi_tvl_before'
    DEFI_TVL_AFTER = 'defi_tvl_after'
    DEFI_TVL_BEFORE_COUNTED = 'defi_tvl_before_counted'
    DEFI_TVL_AFTER_COUNTED = 'defi_tvl_after_counted'
    DEFI_TVL_DELTA = 'defi_tvl_delta_full'
    DEFI_TVL_DELTA_COUNTED = 'defi_tvl_delta'
    DEFI_SQUAD = 'squad'
    DEFI_VOLUME_USD = 'volume_usd'

    TITLE = 'title'
    URL = 'url'


    name: str
    metrics: Dict[str, float]
    score: float = None

@dataclass
class CalculationResults:
    ranking: List[ProjectStat]
    build_time: int

