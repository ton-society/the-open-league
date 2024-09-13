from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
BountyBay app
"""

BountyBay = App(
    name="BountyBay",
    analytics_key="BountyBay",
    url='https://t.me/bountybay_bot',
    metrics=[
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQAjeK7jdhIida6L78_KpOTL4HlY8zOcuqasWkaem1Nv4t1-",
        )
    ]
)
