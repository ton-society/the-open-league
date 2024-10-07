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
            "AUT token mint",
            "EQB0M4CxQIokEEfiyeK6k3KB__ZFs08EP9tewOIk3MycTbql",
            comment_required=True,
        ),
        SmartContractInteraction(
            "Rent lottery",
            "EQAd-gxO1xOW_iSv90u2ZUeW6icI4j1Rdf5M5nK3d5bbKgjD",
            comment_required=True,
        ),
    ],
)
