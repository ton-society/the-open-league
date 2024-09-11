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
            address="EQBStM0V7UrBeohM5cQbiKy40f8z7YgddxsqoKnPVMcoLiDg"
        )
    ]
)
