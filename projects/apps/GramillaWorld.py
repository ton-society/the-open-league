from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
GramillaWorld app
"""

GramillaWorld = App(
    name="Gramilla World",
    analytics_key="GRMLA_BETA",
    url="https://t.me/gramilla_beta_bo",
    metrics=[
        TokenTransferFromUser(
            "Application payment",
            jetton_masters=[
                "EQC47093oX5Xhb0xuk2lCr2RhS8rj-vul61u4W2UH5ORmG_O" # GRAM
            ],
            destinations=[
                "EQD2WYhA6t9LL98JRL63FcKUQDQYD4_y1EU30O_mqG1KbxZU"
            ]
        )
    ]
)
