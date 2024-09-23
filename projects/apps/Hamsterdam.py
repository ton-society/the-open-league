from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Hamsterdam app
"""

Hamsterdam = App(
    name="Hamsterdam",
    analytics_key="Hamsterdam",
    url="https://t.me/HamsterdamPlayBot",
    metrics=[
        SmartContractInteraction(
            "Deposit",
            "EQCfEpfNxxKMPN_r7FvGUimigqvIkcPhVqVTnCuDeN97KXft",
            comment_required=True,
        ),
    ],
)
