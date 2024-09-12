from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Merge Pals app
"""

MergePals = App(
    name="Merge Pals",
    analytics_key="mergepals",
    url="https://t.me/mergepalsbot",
    metrics=[
        SmartContractInteraction(
            "Check-in", "EQBuSCbEWwrULoePEAap4vCV2PJ2CsdgdffIY95E3wJ8snRS", comment_required=True
        ),
    ],
)
