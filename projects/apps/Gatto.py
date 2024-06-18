from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Gatto app
"""

Gatto = App(
    name="Gatto",
    analytics_key="Gatto",
    url='https://t.me/gatto_gamebot',
    metrics=[
        SmartContractInteraction(
            "User actions", "EQBi01YXMYnPnv_rddXJeU4CD47lHyzlZ45JmKObIPL5V9rV", comment_required=True
        ),
        NFTActivity(
            "NFT activity", collections=["EQA2glKDbvezR0KZstAqNmHLEpkOHId1RYAGwza06XLCOLTl"]
        )
        
    ]
)
