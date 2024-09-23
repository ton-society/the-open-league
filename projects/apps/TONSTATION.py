from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
TON STATION app
"""

TONSTATION = App(
    name="TON STATION",
    analytics_key="tonstationgames",
    url="https://t.me/tonstationgames_bot",
    metrics=[
        SmartContractInteraction(
            "Check-in",
            "EQC7m1us8wg8AED2J_L8qq_mtiSSbXZuXu90q0jYqVqRiHK6",
        ),
    ],
)
