from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Televerse Odyssey app
"""

TeleverseOdyssey = App(
    name="Televerse Odyssey",
    analytics_key="Televerse_Odyssey",
    url="https://t.me/TorchOdyssey_bot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQCTK7nQyhjNQUh9lThTzBpt2WHJ-90P_9d8CF4Q041doZdU",
            comment_required=True,
        ),
    ],
)
