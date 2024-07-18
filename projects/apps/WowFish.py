from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
WowFish app
"""

WowFish = App(
    name="WowFish",
    analytics_key="wowfish_game",
    url="https://t.me/WowFishGameBot",
    metrics=[
        SmartContractInteraction(
            "Interaction", 
            address="EQA03lidRjxSQ6CxKpZOpJyqpu0U8XLYyqCF-dJ1aAPgBqYE"
        )
    ]
)
