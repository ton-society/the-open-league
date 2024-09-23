from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Catizen app - https://catizen.ai/
"""

Catizen = App(
    name="Catizen",
    analytics_key="catizen",
    url='https://t.me/catizenbot',
    prizes=False,
    metrics=[
        SmartContractInteraction(
            "Airdop claim", "EQAMl6BVegC0IOZPLhLzWBHCnK4iO4G5eNu4qn_NKQnoISvm"
        ),
        SmartContractInteraction(
            "Boost claim", "EQChB2eMoFG4ThuEsZ6ehlBPKJXOjNxlR5B7qKZNGIv256Da"
        ),
        SmartContractInteraction(
            "New interaction", "EQBj96aEiJlFV4Si16ajonjQRHf_OOb-80WXTOOUTHxd8kDf", comment_required=True
        ),
        TokenTransferFromUser(
            "Token transfer",
            jetton_masters=[
                "EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT", # NOT
                "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs", # USDT
            ],
            destinations=["EQD7UQWKOHYQt5mqVo9JJO-hh0WxrSsNtMTMkg3nVYNafmRO"]
        )

    ]
)
