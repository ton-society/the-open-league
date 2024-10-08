from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Catidpaws app
"""

Cowtopia = App(
    name="Catidpaws",
    analytics_key="Catidpaws",
    url="https://t.me/catidpawsbot",
    metrics=[
        SmartContractInteraction(
            "NFT Receiver",
            "UQBcNjtAn6fju6ndYmKSSK0kNd8yxi4AjV5Hk1W_j00V1LFK",
            comment_required=True,
        ),
        SmartContractInteraction(
            "Early Contributor Receiver",
            "UQAlweUtbOX2mX8FIuyfGwc7SjGnRwzBeMKsLTttW6V1sO2_",
            comment_required=True,
        ),
    ],
)