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
from projects.apps.AKEDOG import AKEDOG
from projects.apps.AKEFish import AKEFish
from projects.apps.Blum import Blum
from projects.apps.Doggers import Doggers
from projects.apps.GHArena import GHArena
from projects.apps.Hamsterdam import Hamsterdam
from projects.apps.HipoGang import HipoGang
from projects.apps.MergePals import MergePals
from projects.apps.Mine2Mine import Mine2Mine
from projects.apps.Molemine import Molemine
from projects.apps.MoonApp import MoonApp
from projects.apps.Nomis import Nomis
from projects.apps.PiggyPiggy import PiggyPiggy
from projects.apps.Randomtg import Randomtg
from projects.apps.SnakeLite import SnakeLite
from projects.apps.StarAI import StarAI
from projects.apps.Tonalytics import Tonalytics
from projects.apps.WONTON import WONTON
from projects.apps.ZenCoin import ZenCoin
from projects.apps.DEPINSIM import DEPINSIM
from projects.apps.HOTWallet import HOTWallet
from projects.apps.MemeTv import MemeTv
from projects.apps.BeeHarvest import BeeHarvest
from projects.apps.GemGame import GemGame
from projects.apps.TeleverseOdyssey import TeleverseOdyssey
from projects.apps.Agent301 import Agent301
from projects.apps.GrandCombat import GrandCombat
from projects.apps.MakeFrens import MakeFrens
from projects.apps.CrazyRushHeroes import CrazyRushHeroes
from projects.apps.TimePrice import TimePrice
from projects.apps.TorchFinance import TorchFinance
from projects.apps.NOTBITCOIN import NOTBITCOIN
from projects.apps.RentTower import RentTower
from projects.apps.RentTycoon import RentTycoon
from projects.apps.TONSTATION import TONSTATION
from projects.apps.Cowtopia import Cowtopia
from projects.apps.Gemz import Gemz
from projects.apps.SEED import SEED
from projects.apps.BOOMUP import BOOMUP
from projects.apps.BUMP import BUMP
from projects.defi.DAOLama import DAOLama
from projects.defi.DeDust import DeDust
from projects.defi.EVAA import EVAA
from projects.defi.GasPump import GasPumpDeFi
from projects.defi.RainbowSwap import RainbowSwap
from projects.defi.StonFi import StonFi
from projects.defi.StormTrade import StormTrade
from projects.defi.Tradoor import Tradoor
from projects.defi.Wonton import Wonton
from projects.defi.SettleTON import SettleTON
from projects.defi.JVault import JVault
from projects.defi.TONHedge import TONHedge
from projects.defi.TonStable import TonStable
from projects.defi.Parraton import Parraton
from projects.defi.TonPools import TonPools
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
from projects.nfts.Crypton import CryptonNFT
from projects.nfts.Diamore import Diamore
from projects.nfts.TheSaudisTON import TheSaudisTONNFT
from projects.nfts.NUTCRACKERS import NUTCRACKERSNFT
from projects.nfts.BIGBALLSBIRDS import BIGBALLSBIRDSNFT
from projects.nfts.FRAM3SALPHABET import FRAM3SALPHABETNFT
from projects.nfts.DigitalResistance import DigitalResistanceNFT
from seasons.app_models import AppLeaderboardModelS6
from seasons.defi_models import DeFiTVLContribution, DeFiVolumeContribution
from seasons.nfts_models import NFTLeaderboardModelV1

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
        AKEDOG,
        AKEFish,
        Blum,
        Doggers,
        GHArena,
        Hamsterdam,
        HipoGang,
        MergePals,
        Mine2Mine,
        Molemine,
        MoonApp,
        Nomis,
        PiggyPiggy,
        Randomtg,
        SnakeLite,
        StarAI,
        Tonalytics,
        WONTON,
        ZenCoin,
        DEPINSIM,
        HOTWallet,
        MemeTv,
        BeeHarvest,
        GemGame,
        TeleverseOdyssey,
        Agent301,
        GrandCombat,
        MakeFrens,
        CrazyRushHeroes,
        TimePrice,
        TorchFinance,
        NOTBITCOIN,
        RentTower,
        RentTycoon,
        TONSTATION,
        Gemz,
        SEED,
        Cowtopia,
        BUMP,
    ],
    score_model=AppLeaderboardModelS6(),
    enrollment_sbt="EQDZ81ZvxRfutjkALcUK0q3Cuusm1XtmhEwUiGSeviLpPARH"
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
        PovelDurevNFT2, TONTanks, CryptonNFT, DigitalResistanceNFT, Diamore, TheSaudisTONNFT,
        NUTCRACKERSNFT, BIGBALLSBIRDSNFT, FRAM3SALPHABETNFT
    ],
    score_model=NFTLeaderboardModelV1()
)

S6_defi_tvl = SeasonConfig(
    leaderboard=SeasonConfig.DEFI,
    name="S6",
    start_time=S6_START,
    end_time=S6_END,
    projects=[
        DAOLama, Tradoor, SettleTON, JVault,
        TONHedge, TonStable, Parraton, TonPools
    ],
    score_model=DeFiTVLContribution(squads=[
        (lambda tvl: tvl >= 5e6, "5M$+"),
        (lambda tvl: tvl >= 1e6, "Under 5M$"),
        (lambda tvl: True, "Under 1M$"),
    ]),
    options={SeasonConfig.OPTION_DEFI_EXCLUDED_POOLS: []}
)

S6_defi_volume = SeasonConfig(
    leaderboard=SeasonConfig.DEFI,
    name="S6",
    start_time=S6_START,
    end_time=S6_END,
    projects=[
        Tradoor, GasPumpDeFi, RainbowSwap
    ],
    score_model=DeFiVolumeContribution(squads=[
        (lambda tvl: tvl >= 50 * 1e6, "50M$+"),
        (lambda tvl: tvl >= 10 * 1e6, "Under 50M$"),
        (lambda tvl: True, "Under 10M$"),
    ])
)
