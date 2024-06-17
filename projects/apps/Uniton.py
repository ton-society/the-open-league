from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Uniton app
"""

Uniton = App(
    name="Uniton",
    analytics_key="Uniton",
    url="https://t.me/UnitonAIBot",
    metrics=[
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQAzEfZT2kiUeTUHiuGIMgKYOFkWtyO8YZlexzE372Y5PYNv",
        )
    ]
)
