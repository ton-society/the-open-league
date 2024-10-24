from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Not Pixel app
"""

NotPixel = App(
    name="Not Pixel",
    analytics_key="NotPixel",
    url="https://t.me/notpixel",
    metrics=[
        SmartContractInteraction(
            "Interaction", 
            address="EQBv3exBKLmQcn2Fm6VlntAInW-je1YP4U59gJxaO62NC37i",
            comment_required=True,
        ),
        TokenTransferFromUser(
            "Token transfer",
            jetton_masters=[
                "EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT", # NOT
                "EQCvxJy4eG8hyHBFsZ7eePxrRsUQSFE_jpptRAYBmcG_DOGS", # DOGS
            ],
            destinations=["EQBv3exBKLmQcn2Fm6VlntAInW-je1YP4U59gJxaO62NC37i"]
        ),
    ]
)
