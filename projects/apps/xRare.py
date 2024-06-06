from models.metrics.nft_activity import NFTActivity
from models.metrics.nft_marketplace import NFTMarketplace
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
xRare app
"""

xRare = App(
    name="xRare",
    analytics_key="xrare",
    metrics=[
        NFTMarketplace("Marketplace sales", "EQD_e1RdLx-t4-D0OCpxzsNFTDRBBpMkMi4TBQEz48awW_qW")
    ]
)
