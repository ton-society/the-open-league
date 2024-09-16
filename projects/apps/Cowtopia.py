from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Cowtopia app
"""

Cowtopia = App(
    name="Cowtopia",
    analytics_key="Cowtopia",
    url="https://t.me/cowtopiabot",
    metrics=[
        SmartContractInteraction(
            "Checkin",
            "EQAnH0qMVcxsFO5e0mZm5AnOFfnDV0-pm6GfjVmtiSfEyLhZ",
            comment_required=True,
        ),
        SmartContractInteraction(
            "Deposit",
            "EQBiAb_CZtd8Q-cBnG3fPm6gRxmnpURMTKvj7P3DdgXPgFP7",
            comment_required=True,
        ),
    ],
)
