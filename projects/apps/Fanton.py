from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Fanton app
"""

Fanton = App(
    name="Fanton",
    analytics_key="Fanton",
    url='https://t.me/FanTonGameBot',
    metrics=[
        NFTActivity(
            "Project NFTs", collections=[
                "EQBpBsShOF1EvuX3nOKwNuzr5YWlJjdpCH_2n8ybizF479Tg",
                "EQCZKrxGwCGUHR7sBgTcADm-JrZR3YccqjDKZwzsSR2SbLL-",
                "EQDfLbr_bJaA_Zb8MQsS_RIrHKBG6gYCSO_C48b7JJHCUYi-"
            ]
        ),
        SmartContractInteraction(
            "Deposits", "EQB7GLGF3Xng2kMKLInjq7VWkz8qie8pQtZd1Z8EaqyCIYTw", comment_not_equals=['', 'Royalty']
        ),
        SmartContractInteraction(
            "cNFT mint", "EQApZPOrKned6Ydct3TZelVcTl0-DlNjc2pxAzVzSPf3jiPA", op_codes=[20593830]
        )
    ]
)
