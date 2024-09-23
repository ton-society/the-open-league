from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
AKEDOG app
"""

AKEDOG = App(
    name="AKEDOG",
    analytics_key="Akedo_clicker",
    url="https://t.me/Akedo_Bot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQBPfUOQuEMMX4idrPWATlQ1IKmbPFeYmFWcJuk4CuXHjUzg",
            comment_required=True,
        ),
    ],
)
