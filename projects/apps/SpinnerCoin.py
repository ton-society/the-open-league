from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
SpinnerCoin app
"""

SpinnerCoin = App(
    name="SpinnerCoin",
    analytics_key="SpinnerCoin",
    url="http://t.me/SpinnerCoin_bot",
    metrics=[
        SmartContractInteraction(
            "Interaction", 
            address="EQDb21gSN-22SGD5TYXvok81BzRsc0autQji8prcH0zoNlF2"
        )
    ]
)
