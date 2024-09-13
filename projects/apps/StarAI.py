from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
StarAI app
"""

StarAI = App(
    name="StarAI",
    analytics_key="OnlineStarAI",
    url="https://t.me/TheStarAIBot",
    nfts=["EQBzi2u9CZ0KIIMKWouYtHlzqzBxvGwvgedsWgEwFWdg_HyR"],
    metrics=[
        SmartContractInteraction(
            "Сheck-in", "EQCxr1o-x7cEFb3vALiYMOW7QPuAoGHMtw1Yab5m6HrnuIuZ"
        ),
    ],
)
