"""
S5 season config
"""
from models.season_config import SeasonConfig, DexPool
from projects.apps.Arbuz import Arbuz
from projects.apps.BountyBay import BountyBay
from projects.apps.CatGoldMiner import CatGoldMiner
from projects.apps.Catizen import Catizen
from projects.apps.Sphynx import Sphynx
from projects.apps.ChickCoop import ChickCoop
from projects.apps.EdChess import EdChess
from projects.apps.Fanton import Fanton
from projects.apps.Fanzee import Fanzee
from projects.apps.GM import GM
from projects.apps.Gamee import Gamee
from projects.apps.Gatto import Gatto
from projects.apps.GetGems import GetGems
from projects.apps.Gleam import Gleam
from projects.apps.Gram import Gram
from projects.apps.GramillaWorld import GramillaWorld
from projects.apps.JetTon import JetTon
from projects.apps.MomoAI import MomoAI
from projects.apps.MoneyGardenAI import MoneyGardenAI
from projects.apps.PlayWallet import PlayWallet
from projects.apps.QuackQuack import QuackQuack
from projects.apps.Shardify import Shardify
from projects.apps.SquidTG import SquidTG
from projects.apps.SwapCoffee import SwapCoffee
from projects.apps.TonMap import TonMap
from projects.apps.TonPunks import TonPunks
from projects.apps.TonUp import TonUP
from projects.apps.Tonano import Tonano
from projects.apps.Tongochi import Tongochi
from projects.apps.TonsOfFriends import TonsOfFriends
from projects.apps.Uniton import Uniton
from projects.apps.Vertus import Vertus
from projects.apps.XPLUS import XPLUS
from projects.apps.YesCoin import YesCoin
from projects.apps.xRare import xRare
from projects.defi.DAOLama import DAOLama
from projects.defi.DeDust import DeDust
from projects.defi.EVAA import EVAA
from projects.defi.StonFi import StonFi
from projects.defi.StormTrade import StormTrade
from projects.defi.Tradoor import Tradoor
from projects.tokens.ARBUZ import ARBUZ
from projects.tokens.KINGY import KINGY
from projects.tokens.NOT import NOT
from projects.tokens.PUNK import PUNK
from projects.tokens.GLINT import GLINT
from projects.tokens.RECA import RECA
from projects.tokens.TIGER import TIGER
from projects.tokens.WALL import WALL
from projects.tokens.DFC import DFC
from projects.tokens.MEH import MEH
from projects.tokens.HYDRA import HYDRA
from projects.tokens.WEB3 import WEB3
from projects.tokens.STON import STON
from projects.tokens.BOLT import BOLT
from projects.tokens.durev import durev
from projects.tokens.OPEN import OPEN
from projects.tokens.TGRAM import TGRAM
from projects.tokens.MagicCrystal import MagicCrystal
from projects.tokens.TONG import TONG
from projects.tokens.SCALE import SCALE
from projects.tokens.GRAM import GRAM
from projects.tokens.VIRUS import VIRUS
from projects.tokens.JVT import JVT
from projects.tokens.BURN import BURN
from projects.tokens.UP import UP
from projects.tokens.GEMSTON import GEMSTON
from projects.tokens.SQD import SQD
from projects.tokens.CATS import CATS
from projects.tokens.RUSD import RUSD
from projects.tokens.REDO import REDO
from projects.tokens.Bear import Bear
from projects.tokens.MEM import MEM
from projects.tokens.FNZ import FNZ
from projects.tokens.SHIP import SHIP
from projects.tokens.LAVE import LAVE
from projects.tokens.TONK import TONK
from projects.tokens.CES import CES
from projects.tokens.TON_STARS import TON_STARS
from projects.tokens.SOX import SOX
from projects.tokens.COFE import COFE
from projects.tokens.PEPE import PEPE
from projects.tokens.REGI import REGI
from projects.tokens.WIF import WIF
from projects.tokens.ANON import ANON
from projects.tokens.KAKAXA import KAKAXA
from projects.tokens.JETTON import JETTON
from projects.tokens.FISH import FISH
from projects.tokens.DICK import DICK
from projects.tokens.LLAMA import LLAMA
from projects.tokens.TONALD import TONALD
from projects.tokens.MITTENS import MITTENS
from projects.tokens.WON import WON
from projects.tokens.HIF import HIF
from projects.tokens.RANDOM import RANDOM
from projects.tokens.INS import INS
from projects.tokens.SHIT import SHIT
from projects.tokens.POE import POE
from projects.nfts.TheMinersClubNFTs import TheMinersClubNFTsNFT
from projects.nfts.YNGEXPLRZ import YNGEXPLRZNFT
from projects.nfts.Gatto import GattoNFT
from projects.nfts.AnimalsRedList import AnimalsRedListNFT
from projects.nfts.Smeshariki import SmesharikiNFT
from projects.nfts.TONDiamonds import TONDiamondsNFT
from projects.nfts.NOTPunks import NOTPunksNFT
from projects.nfts.TONFISHBOX import TONFISHBOXNFT
from projects.nfts.PovelDurevNFT import PovelDurevNFTNFT
from projects.nfts.TONPunks import TONPunksNFT
from projects.nfts.TonedApeClub import TonedApeClubNFT
from projects.nfts.Runeston import RunestonNFT
from projects.nfts.FantonFantasyFootball import FantonFantasyFootballNFT
from projects.nfts.RoOLZ import RoOLZNFT
from projects.nfts.Glitches import GlitchesNFT
from projects.nfts.MarketMakers import MarketMakers
from projects.nfts.Parachute import Parachute
from projects.nfts.NFTWeb3TON import NFTWeb3TON
from projects.nfts.TONFrogs import TONFrogs
from projects.nfts.GBOTSSD import GBOTSSD
from projects.nfts.TonAlchemists import TonAlchemists
from projects.nfts.TONSharks import TONSharks
from seasons.app_models import AppLeaderboardModelV2, AppLeaderboardModelV3
from seasons.defi_models import DeFiWeightedRewards
from seasons.nfts_models import NFTLeaderboardModelV1
from seasons.tokens_models import TokenLeaderboardModelV4, TokenLeaderboardModelV5

S5_START = 1720609200 # Wed Jul 10 2024 11:00:00 GMT+0000
S5_END = 1723028400 # Wed Aug 7 2024 11:00:00 GMT+0000

S5_apps = SeasonConfig(
    leaderboard=SeasonConfig.APPS,
    name="S5",
    start_time=S5_START,
    end_time=S5_END,
    projects=[
        QuackQuack,
        Arbuz,
        Fanzee,
        Catizen,
        Sphynx,
        GM,
        JetTon,
        SquidTG,
        XPLUS,
        xRare,
        PlayWallet,
        YesCoin,
        GetGems,
        Fanton,
        Tonano,
        TonPunks,
        SwapCoffee,
        Gram,
        Gatto,
        TonsOfFriends,
        ChickCoop,
        TonUP,
        Tongochi,
        Shardify,
        TonMap,
        Gamee,
        MoneyGardenAI,
        BountyBay,
        CatGoldMiner,
        Vertus,
        Uniton,
        EdChess,
        GramillaWorld,
        MomoAI,
        Gleam,
    ],
    score_model=AppLeaderboardModelV3()
)

S5_tokens = SeasonConfig(
    leaderboard=SeasonConfig.TOKENS,
    name="S5",
    start_time=S5_START,
    end_time=S5_END,
    projects=[
        ARBUZ, KINGY, PUNK, GLINT, RECA, TIGER, WALL, DFC, MEH, HYDRA, WEB3, STON, BOLT,
        durev, OPEN, TGRAM, MagicCrystal, TONG, SCALE, GRAM, VIRUS, JVT, BURN, UP,
        GEMSTON, SQD, CATS, RUSD, REDO, Bear, MEM,
        FNZ, SHIP, LAVE, TONK, CES, TON_STARS, SOX, COFE, PEPE, REGI, WIF, ANON,
        KAKAXA, JETTON, FISH, DICK, LLAMA, TONALD, WON, HIF, RANDOM, INS, SHIT, POE, MITTENS,
        NOT
    ],
    score_model=TokenLeaderboardModelV5()
)

S5_nfts = SeasonConfig(
    leaderboard=SeasonConfig.NFTS,
    name="S5",
    start_time=S5_START,
    end_time=S5_END,
    projects=[
        TheMinersClubNFTsNFT, YNGEXPLRZNFT, GattoNFT, AnimalsRedListNFT, SmesharikiNFT,
        TONDiamondsNFT, NOTPunksNFT, TONFISHBOXNFT, PovelDurevNFTNFT, TONPunksNFT,
        TonedApeClubNFT, RunestonNFT, FantonFantasyFootballNFT, RoOLZNFT, GlitchesNFT,
        MarketMakers, Parachute, NFTWeb3TON, TONFrogs, GBOTSSD, TonAlchemists, TONSharks

    ],
    score_model=NFTLeaderboardModelV1()
)

S5_defi = SeasonConfig(
    leaderboard=SeasonConfig.DEFI,
    name="S5",
    start_time=S5_START,
    end_time=S5_END,
    projects=[
        DeDust, StonFi, DAOLama, StormTrade, EVAA, Tradoor
    ],
    score_model=DeFiWeightedRewards(
        total_prize_pool=150000,
        max_prize=75000
    ),
    options={
        SeasonConfig.OPTION_DEFI_EXCLUDED_POOLS: [
            DexPool(  # USDT/TON
                address='EQA-X_yo3fzzbDbJ_0bzFWKqtRuZFIRa1sJsveZJ1YpViO3r',
                dex=DexPool.DEX_DEDUST,
                asset_position=DexPool.POSITION_RIGHT,
                asset_currency=DexPool.ASSET_USDT
            ),
            DexPool(  # USDT/TON
                address='EQD8TJ8xEWB1SpnRE4d89YO3jl0W0EiBnNS4IBaHaUmdfizE',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_LEFT,
                asset_currency=DexPool.ASSET_USDT
            ),
            ### TOL Projects boosts
            ### DeDust
            DexPool(  # BOLT/TON
                address='EQABHkxndSnqrBgMIDR73LB0FBDDM0C_Up39EL1Rn3ao_54-',
                dex=DexPool.DEX_DEDUST,
                asset_position=DexPool.POSITION_LEFT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # HYDRA/TON
                address='EQBF-YYoDy6ue0J4K-v5L_HYzwWCLpwXSLsTFmT7hr2uqHf5',
                dex=DexPool.DEX_DEDUST,
                asset_position=DexPool.POSITION_LEFT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # JVT/TON
                address='EQB7zhVOQKkfoMtnGU4f_uf0f6HmgcHJj6vZ-NTyHhsaPHCo',
                dex=DexPool.DEX_DEDUST,
                asset_position=DexPool.POSITION_LEFT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # KINGY/TON
                address='EQDsIxN6kTHNTzkW-KDAFoOd7uK8IV_qhw8wR5NkYH1Gh_SQ',
                dex=DexPool.DEX_DEDUST,
                asset_position=DexPool.POSITION_LEFT,
                asset_currency=DexPool.ASSET_TON
            ),
            ## Ston.fi
            DexPool(  # WEB3/TON
                address='EQBeplxseh8R1QHlFwuCHiUnm7Mhp5aAQ7_n7-n5iXlhCThc',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_LEFT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # FNZ/TON
                address='EQAZFS5dJ8STrKcn5VnptYsoKILXbAYaDhdJJjbzUrNkDdH_',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_RIGHT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # STON/TON
                address='EQDtZHOtVWaf9UIU6rmjLPNLTGxNLNogvK5xUZlMRgZwQ4Gt',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_RIGHT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # WALL/TON
                address='EQAI2oFhkFupg6tHRpKwxbVNQbHwuD7HlSCkHD6vi2V--8_0',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_RIGHT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # COFE/TON
                address='EQDsMul-_xm99ien8PGbIg5BDBNhwI_RJAfzx8yxjZDiNgCA',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_RIGHT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # JETTON/TON
                address='EQATnq6W2xv10C19LNlC26xFtTV1fbzMkXmXQCWHqtv6Okf7',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_LEFT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # DFC/TON
                address='EQCmapEiLQO0uYEOmvDeXNR9i5R4kYVPEmyNJEcwSCTSUTTa',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_RIGHT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # durev/TON
                address='EQAIp9JcWs87eXXuaTaDXxzQSoN6yt4pffqxy1hXWBBmguqq',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_LEFT,
                asset_currency=DexPool.ASSET_TON
            ),
            DexPool(  # LLAMA/TON
                address='EQC6Tw4JSRKlqVx5Qn_-wgKXCn0E_ikza9MdtqSwzl-W65TR',
                dex=DexPool.DEX_STON,
                asset_position=DexPool.POSITION_RIGHT,
                asset_currency=DexPool.ASSET_TON
            ),
        ]
    },
    block_before_start_ref='TODO'
)
