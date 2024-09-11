from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
GramillaWorld app
"""

GramillaWorld = App(
    name="Gramilla World",
    analytics_key="GRMLA_BETA",
    url="https://t.me/gramilla_worldBot",
    metrics=[
        TokenTransferFromUser(
            "Application payment",
            jetton_masters=[
                "EQC47093oX5Xhb0xuk2lCr2RhS8rj-vul61u4W2UH5ORmG_O" # GRAM
            ],
            destinations=[
                "EQBDBA01I7q00LPi_VVI1NwL6YH2HV3B4M7zf1JibpSUDXzs"
            ]
        )
    ]
)
