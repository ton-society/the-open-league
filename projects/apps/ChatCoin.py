from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
ChatCoin app
"""

ChatCoin = App(
    name="ChatCoin",
    analytics_key="ChatCoin",
    url="https://t.me/ChatCoinAppBot",
    metrics=[
        SmartContractInteraction(
            "Check-in",
            "EQA74Q8ktV6KdYOab0rAaauiYnEh6L9ThlG7uwFk1cuNQvKm",
        ),
    ],
)
