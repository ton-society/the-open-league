from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
GramillaWorld app
"""

GramillaWorld = App(
    name="Gramilla World",
    analytics_key="GRMLA_BETA",
    url="https://t.me/gramilla_beta_bo",
    metrics=[
        SmartContractInteraction(
            "Application payment", 
            address="EQD2WYhA6t9LL98JRL63FcKUQDQYD4_y1EU30O_mqG1KbxZU",
        )
    ]
)
