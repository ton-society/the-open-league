from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Grand Combat app
"""

GrandCombat = App(
    name="Grand Combat",
    analytics_key="GrandCombat",
    url="https://t.me/grandcombat_bot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQAIcNCVhsldWIdyxHO3oIrGA3GOuFeDrk3xxTtOFknl4E-z",
            op_codes=[1495321901]
        ),
    ],
)
