from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
gemz app
"""

Gemz = App(
    name="gemz",
    analytics_key="gemz",
    url="https://t.me/gemzcoin_bot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQC_0ScHnb7bVoyInXLkZ2G4XRHg97S9XrPKCUDaO1ZRyFhZ",
            comment_required=True,
        ),
    ],
)
