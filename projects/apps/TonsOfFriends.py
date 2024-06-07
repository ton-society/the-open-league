from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
TonsOfFriends app
"""

TonsOfFriends = App(
    name="TonsOfFriends",
    analytics_key=None,
    metrics=[
        SmartContractInteraction(
            "Contract calls", "EQBUXXx7QXeogpRqlCEqvJrhLKLmLrJKqnB35V931v2gYdW-",
            op_codes=[465513156, -1852192293]
        )
    ]
)
