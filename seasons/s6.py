"""
S6 season config
"""
from models.season_config import SeasonConfig, DexPool
from projects.apps.BountyBay import BountyBay
from projects.apps.CatGoldMiner import CatGoldMiner
from projects.apps.Catizen import Catizen
from projects.apps.CatXWar import CatXWar
from projects.apps.ChickCoop import ChickCoop
from projects.apps.EdChess import EdChess
from projects.apps.Fanton import Fanton
from projects.apps.Fanzee import Fanzee
from projects.apps.Gamee import Gamee
from projects.apps.GasPump import GasPump
from projects.apps.Gatto import Gatto
from projects.apps.GetGems import GetGems
from projects.apps.Gleam import Gleam
from projects.apps.Gram import Gram
from projects.apps.GramillaWorld import GramillaWorld
from projects.apps.JetTon import JetTon
from projects.apps.MomoAI import MomoAI
from projects.apps.MoneyGardenAI import MoneyGardenAI
from projects.apps.PlayWallet import PlayWallet
from projects.apps.Pumpers import Pumpers
from projects.apps.QuackQuack import QuackQuack
from projects.apps.Shardify import Shardify
from projects.apps.Sphynx import Sphynx
from projects.apps.SpinnerCoin import SpinnerCoin
from projects.apps.SquidTG import SquidTG
from projects.apps.SwapCoffee import SwapCoffee
from projects.apps.TonMap import TonMap
from projects.apps.TonPunks import TonPunks
from projects.apps.TonUp import TonUP
from projects.apps.Tonano import Tonano
from projects.apps.TonGifts import TonGifts
from projects.apps.Tongochi import Tongochi
from projects.apps.TonsOfFriends import TonsOfFriends
from projects.apps.TypoCurator import TypoCurator
from projects.apps.Uniton import Uniton
from projects.apps.Vertus import Vertus
from projects.apps.WheelOfFate import WheelOfFate
from projects.apps.WowFish import WowFish
from projects.apps.XPLUS import XPLUS
from projects.apps.YesCoin import YesCoin
from projects.apps.xRare import xRare
from projects.defi.DAOLama import DAOLama
from projects.defi.DeDust import DeDust
from projects.defi.EVAA import EVAA
from projects.defi.StonFi import StonFi
from projects.defi.StormTrade import StormTrade
from projects.defi.Tradoor import Tradoor
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
from projects.tokens.DMT import DMT
from projects.tokens.Spotty import Spotty
from projects.tokens.PLANE  import PLANE
from projects.tokens.UTYA import UTYA
from projects.tokens.M5 import M5
from projects.tokens.TDOG import TDOG
from projects.tokens.GLITCH import GLITCH
from projects.tokens.RUS import RUS
from projects.tokens.BTC25 import BTC25
from projects.tokens.MY import MY
from projects.tokens.OR import OR
from projects.tokens.MAN import MAN
from projects.tokens.DYOR import DYOR
from projects.tokens.CAVI import CAVI
from projects.tokens.PET import PET
from projects.tokens.CRYPTON import CRYPTON
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
from projects.nfts.PovelDurevNFT2 import PovelDurevNFT2
from projects.nfts.TONTanks import TONTanks
from seasons.app_models import AppLeaderboardModelV2, AppLeaderboardModelV3
from seasons.defi_models import DeFiWeightedRewards
from seasons.nfts_models import NFTLeaderboardModelV1
from seasons.tokens_models import TokenLeaderboardModelV4, TokenLeaderboardModelV5

S6_START = 1726138800 # Thu Sep 12 2024 11:00:00 GMT+0000
S6_END = 1728558000 # Thu Oct 10 2024 11:00:00 GMT+0000

S6_apps = SeasonConfig(
    leaderboard=SeasonConfig.APPS,
    name="S6",
    start_time=S6_START,
    end_time=S6_END,
    projects=[
        QuackQuack,
        Fanzee,
        Catizen,
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
        CatXWar,
        WheelOfFate,
        TypoCurator,
        Sphynx,
        SpinnerCoin,
        GasPump,
        TonGifts,
        Pumpers,
        WowFish,
    ],
    score_model=AppLeaderboardModelV3()
)

S6_nfts = SeasonConfig(
    leaderboard=SeasonConfig.NFTS,
    name="S6",
    start_time=S6_START,
    end_time=S6_END,
    projects=[
        TheMinersClubNFTsNFT, YNGEXPLRZNFT, GattoNFT, AnimalsRedListNFT, SmesharikiNFT,
        TONDiamondsNFT, NOTPunksNFT, TONFISHBOXNFT, PovelDurevNFTNFT, TONPunksNFT,
        TonedApeClubNFT, RunestonNFT, FantonFantasyFootballNFT, RoOLZNFT, GlitchesNFT,
        MarketMakers, Parachute, NFTWeb3TON, TONFrogs, GBOTSSD, TonAlchemists, TONSharks,
        PovelDurevNFT2, TONTanks

    ],
    score_model=NFTLeaderboardModelV1()
)