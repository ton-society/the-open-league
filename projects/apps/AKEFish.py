from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
AKEFish app
"""

AKEFish = App(
    name="AKEFish",
    analytics_key="Akefish",
    url="https://t.me/AKEFishBot",
    metrics=[
        SmartContractInteraction(
            "Сheck-in", "EQA8gfa96Qrzpdwn_FvkCQa35MNCr1L77HNRpOOeQLgV3k7v", comment_required=True
        ),
    ],
)
