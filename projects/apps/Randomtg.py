from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Random.tg app
"""

Randomtg = App(
    name="Random.tg",
    analytics_key="random",
    url="https://random.tg",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQAqLHxYEHrnn6WAtrlj1Z8PsnQyn6YV9YWDcor2X4RANDOM",
        ),
    ],
)
