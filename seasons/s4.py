"""
S4 season config
"""
from models.season_config import SeasonConfig
from projects.apps.Arbuz import Arbuz
from projects.apps.Catizen import Catizen
from projects.apps.ChickCoop import ChickCoop
from projects.apps.Fanton import Fanton
from projects.apps.Fanzee import Fanzee
from projects.apps.GM import GM
from projects.apps.Gatto import Gatto
from projects.apps.GetGems import GetGems
from projects.apps.Gram import Gram
from projects.apps.JetTon import JetTon
from projects.apps.PlayWallet import PlayWallet
from projects.apps.QuackQuack import QuackQuack
from projects.apps.RoyalFortress import RoyalFortress
from projects.apps.Shardify import Shardify
from projects.apps.SquidTG import SquidTG
from projects.apps.SwapCoffee import SwapCoffee
from projects.apps.TapFantasy import TapFantasy
from projects.apps.ThePixels import ThePixels
from projects.apps.TonPunks import TonPunks
from projects.apps.TonUp import TonUP
from projects.apps.Tonano import Tonano
from projects.apps.Tongochi import Tongochi
from projects.apps.TonsOfFriends import TonsOfFriends
from projects.apps.XPLUS import XPLUS
from projects.apps.YesCoin import YesCoin
from projects.apps.xRare import xRare
from projects.tokens.ARBUZ import ARBUZ
from projects.tokens.KINGY import KINGY
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
from seasons.app_models import AppLeaderboardModelV2
from seasons.nfts_models import NFTLeaderboardModelV1
from seasons.tokens_models import TokenLeaderboardModelV4

S4_START = 1718190000 # Wed Jun 12 2024 11:00:00 GMT+0000
S4_END = 1719399600 # Wed Jun 26 2024 11:00:00 GMT+0000

S4_apps = SeasonConfig(
    leaderboard=SeasonConfig.APPS,
    name="S4",
    start_time=S4_START,
    end_time=S4_END,
    projects=[
        QuackQuack,
        Arbuz,
        Fanzee,
        Catizen,
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
        RoyalFortress,
        TonsOfFriends,
        ChickCoop,
        TapFantasy,
        ThePixels,
        TonUP,
        Tongochi,
        Shardify
    ],
    score_model=AppLeaderboardModelV2()
)

S4_tokens = SeasonConfig(
    leaderboard=SeasonConfig.TOKENS,
    name="S4",
    start_time=S4_START,
    end_time=S4_END,
    projects=[
        ARBUZ, KINGY, PUNK, GLINT, RECA, TIGER, WALL, DFC, MEH, HYDRA, WEB3, STON, BOLT,
        durev, OPEN, TGRAM, MagicCrystal, TONG, SCALE, GRAM, VIRUS, JVT, BURN, UP,
        GEMSTON, SQD, CATS, RUSD, REDO, Bear, MEM,
        FNZ, SHIP, LAVE, TONK, CES, TON_STARS, SOX, COFE, PEPE, REGI, WIF, ANON,
        KAKAXA, JETTON, FISH, DICK, LLAMA, TONALD
    ],
    score_model=TokenLeaderboardModelV4()
)

S4_nfts = SeasonConfig(
    leaderboard=SeasonConfig.NFTS,
    name="S4",
    start_time=S4_START,
    end_time=S4_END,
    projects=[
        TheMinersClubNFTsNFT, YNGEXPLRZNFT, GattoNFT, AnimalsRedListNFT, SmesharikiNFT,
        TONDiamondsNFT, NOTPunksNFT, TONFISHBOXNFT, PovelDurevNFTNFT, TONPunksNFT,
        TonedApeClubNFT, RunestonNFT, FantonFantasyFootballNFT, RoOLZNFT, GlitchesNFT

    ],
    score_model=NFTLeaderboardModelV1()
)