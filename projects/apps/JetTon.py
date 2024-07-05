from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.metrics.token_transfer_to_user import TokenTransferToUser
from models.project import App
from projects.tokens.JETTON import JETTON

"""
JetTon app
"""

JetTon = App(
    name="JetTon",
    analytics_key="qqqq", # o_O
    url='https://t.me/jetton', 
    metrics=[
        TokenTransferFromUser(
            "Deposits in Jetton",
            jetton_masters=[
                "EQAQXlWJvGbbFfE8F3oS8s87lIgdovS455IsWFaRdmJetTon" # JetTon
            ],
            destinations=[
                "EQA7IvmhA3UnbXgKoFZjgLmPtKomEcWH-TEIz8vonFwahcha"
            ]
        )
    ],
    token=JETTON
)
