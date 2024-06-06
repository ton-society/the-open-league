from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
XPLUS app
"""

XPLUS = App(
    name="XPLUS",
    analytics_key="XPLUS",
    metrics=[
        SmartContractInteraction(
            "Check-in", "EQCU80ddWxsL0JFiRh3pYxDqwPG777t4qDBv6wde7MpsyJTH", op_codes=[1699364067]
        ),
        SmartContractInteraction(
            "Deposits and withdrawals", "EQBUeNPXALePbqkBLIGyIGIGyeYgd7pZzBmQHIumaLxzjgEB", op_codes=[1076884676, -1552920267]
        ),
        NFTActivity(
            "NFT activity", collections=["EQD4-peNeFh7IqZdy-oXoyoHoPVyNP0K1RNY3xTeYj8tenCP"]
        )
        
    ]
)
