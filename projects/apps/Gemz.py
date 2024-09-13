from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
gemz app
"""

Gemz = App(
    name="gemz",
    analytics_key="gemz",
    url="https://t.me/gemzcoin_bot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQBj4jX-6KSEY5oFd98sdIZB5YrnOWIOvskD_Mf8VuJ4EAeB",
            op_codes=[-1959520222],
        ),
    ],
)
