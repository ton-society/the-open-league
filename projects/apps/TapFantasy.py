from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
TAP FANTASY app
"""

TapFantasy = App(
    name="TAP FANTASY",
    analytics_key=None,
    metrics=[
        SmartContractInteraction(
            "On-chain check in", "EQB52lJbxS_RIgl19lDZYToT-Je6YwJfXF-2aKk4bh1Bj_xp"
        ),
        NFTActivity(
            "NFT activity", collections=["EQBHG9ChK3CHRuCD5-561t6Z7nV7hub-gF6Z7pdVpqcnR4gJ"]
        )
    ]
)
