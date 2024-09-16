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
            "EQBCC49AnXkwfpVhTf45xPOdBUzZR8P_-woQiEoUnzN4VhCS",
            comment_required=True,
        ),
    ],
)
