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
            address="EQAzIUFN8MJ3cGQiKBqHr-COHAz0D7fNnCD2kHneJxmK9gPd",
        ),
        SmartContractInteraction(
            "USDT Reward Claim", 
            address="EQCicS0nUozy2zuYHRuIV8L2UCFwb8eQZ3g0JpG9BsiCbMhv",
        )
    ]
)
