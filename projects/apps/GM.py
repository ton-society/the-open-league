from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.metrics.token_transfer_to_user import TokenTransferToUser
from models.project import App

"""
GM app
"""

GM = App(
    name="GM",
    analytics_key="KINGY",
    prizes=False,
    url='https://t.me/kingyGMbot',
    metrics=[
        TokenTransferToUser(
            "Claims", sources=["EQAfzTHykeqA3uN_w8Naoluqx2CHOU5NllD8oK5S5ZYiqNR3"]
        ),
        TokenTransferFromUser(
            "Boosts", destinations=["EQAfzTHykeqA3uN_w8Naoluqx2CHOU5NllD8oK5S5ZYiqNR3"]
        )
    ]
)
