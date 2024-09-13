from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
GemGame app
"""

GemGame = App(
    name="GemGame",
    analytics_key="gem_game",
    url="https://t.me/play_gemgame_bot/play?startapp=c_tw",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQDJT5TJ6BpL2tFHKdh4oRxbhW3LXwsdwSE0FO9jsLV0A3Db",
        ),
    ],
)
