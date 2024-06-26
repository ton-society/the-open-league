from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Gamee app
"""

Gamee = App(
    name="Gamee",
    analytics_key="Gamee",
    url='https://www.gamee.com/',
    metrics=[
        SmartContractInteraction(
            "Interaction", "EQBVxA9MkwWmfq46bv9-ikOQHXgelaFTvIo9gtR9ZLn0VoeS"
        ),
    ]
)
