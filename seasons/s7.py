"""
S7 season config
"""
from models.season_config import SeasonConfig
from projects.defi.Beetroot import Beetroot
from projects.defi.Delea import Delea
from projects.defi.UTONIC import UTONIC
from projects.defi.Farmix import Farmix
from projects.defi.Coffin import Coffin
from projects.defi.SwapCoffee import SwapCoffeeVolume, SwapCoffeeTVL
from projects.defi.AquaProtocol import AquaProtocol
from projects.defi.Crouton import Crouton
from projects.defi.DAOLama import DAOLama
from projects.defi.GasPump import GasPumpDeFi
from projects.defi.Moki import Moki
from projects.defi.RainbowSwap import RainbowSwap
from projects.defi.SettleTON import SettleTON
from projects.defi.JVault import JVault
from projects.defi.Titan import Titan
from projects.defi.TONCO import TONCO
from projects.defi.TONHedge import TONHedge
from projects.defi.TonStable import TonStable
from projects.defi.Parraton import Parraton
from projects.defi.TonPools import TonPools
from seasons.defi_models import DeFiTVLContribution, DeFiVolumeContribution


S7_START = 1732705200 # Wed Nov 27 2024 11:00:00 GMT+0000
S7_END = 1734433200 # Tue Dec 17 2024 11:00:00 GMT+0000


S7_defi_tvl = SeasonConfig(
    leaderboard=SeasonConfig.DEFI,
    name="S7",
    start_time=S7_START,
    end_time=S7_END,
    projects=[
        DAOLama, SettleTON, JVault,
        TONHedge, TonStable, Parraton, TonPools,
        AquaProtocol, SwapCoffeeTVL, Coffin, TONCO, Farmix,
        Crouton, Delea
    ],
    score_model=DeFiTVLContribution(squads=[
        (lambda tvl: tvl >= 5e6, "Over 5M$"),
        (lambda tvl: tvl >= 1e6, "Under 5M$"),
        (lambda tvl: True, "Under 1M$"),
    ]),
    options={SeasonConfig.OPTION_DEFI_EXCLUDED_POOLS: []}
)

S7_defi_volume = SeasonConfig(
    leaderboard=SeasonConfig.DEFI,
    name="S7",
    start_time=S7_START,
    end_time=S7_END,
    projects=[
        GasPumpDeFi, RainbowSwap, SwapCoffeeVolume, Moki, Titan
    ],
    score_model=DeFiVolumeContribution(squads=[
        (lambda tvl: tvl >= 50 * 1e6, "Over 50M$"),
        (lambda tvl: tvl >= 10 * 1e6, "Under 50M$"),
        (lambda tvl: True, "Under 10M$"),
    ])
)
