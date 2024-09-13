from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Rent Tycoon app
"""

RentTycoon = App(
    name="Rent Tycoon",
    analytics_key="Rent_Tycoon",
    url="https://t.me/rent_tycoon_bot",
    metrics=[
        SmartContractInteraction(
            "Payment",
            "EQB0M4CxQIokEEfiyeK6k3KB__ZFs08EP9tewOIk3MycTbql",
            comment_required=True,
        ),
    ],
)
