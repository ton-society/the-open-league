from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Agent 301 app
"""

Agent301 = App(
    name="Agent 301",
    analytics_key="Agent301",
    url="https://t.me/Agent301Bot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQB_a4Y-9OYfcAsI7Evvyf7ph59mQrNFeqLwNBIPJkEFS-gb",
        ),
    ],
)
