from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
BeeHarvest app
"""

BeeHarvest = App(
    name="BeeHarvest",
    analytics_key="BeeharvestProd",
    url="https://t.me/beeharvestbot",
    nfts=["EQDVJADeL16Dv-alWpWFSgQrP-IqGjcNrJwQH65bXgBzKt8C"],
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQC6q99HyVc1GGLKOYfh_3ztYddYF-ir4-C92gusWcASs0TS",
            comment_required=True,
        ),
    ],
)
