from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Rent Tower app
"""

RentTower = App(
    name="Rent Tower",
    analytics_key="Rent_Tycoon_Game",
    url="https://t.me/Rent_Tower_Game_bot",
    metrics=[
        SmartContractInteraction(
            "Payment",
            "EQBvlltkYThhbU5ZoWz1YY-XEFGoCW9pVdVBhHyrWJzGa2KG",
            comment_required=True,
        ),
    ],
)
