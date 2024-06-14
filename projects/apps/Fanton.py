from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Fanton app
"""

Fanton = App(
    name="FantonTESTICONS",
    analytics_key="Fanton",
    metrics=[
        NFTActivity(
            "Project NFTs", collections=[
                "EQBpBsShOF1EvuX3nOKwNuzr5YWlJjdpCH_2n8ybizF479Tg",
                "EQCZKrxGwCGUHR7sBgTcADm-JrZR3YccqjDKZwzsSR2SbLL-"
            ]
        ),
        SmartContractInteraction(
            "Deposits", "EQB7GLGF3Xng2kMKLInjq7VWkz8qie8pQtZd1Z8EaqyCIYTw", comment_not_equals=['', 'Royalty']
        )
    ]
)
