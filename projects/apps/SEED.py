from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
SEED app
"""

SEED = App(
    name="SEED",
    analytics_key="seed_analytics",
    url="",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQAO7qlEW3-KU6X64LpXKK2h2-vG-wrLNB-w9hnuFNrO0lIk",
            comment_required=True,
        ),
    ],
)
