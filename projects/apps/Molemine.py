from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
molemine app
"""

Molemine = App(
    name="molemine",
    analytics_key="molemine",
    url="https://t.me/moleminebot",
    metrics=[
        SmartContractInteraction(
            "Сheck-in", "EQCpZ6jzUoJjiZuMmaKqgqlxZZT32hvBSfzb8ixXbgsYOGya"
        ),
    ],
)
