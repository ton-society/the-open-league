from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
SnakeLite app
"""

SnakeLite = App(
    name="SnakeLite",
    analytics_key="Snakelite",
    url="https://t.me/Snakelite_official_bot",
    metrics=[
        SmartContractInteraction(
            "Payment", "EQAgZ4oUgnd5MfpziNv600cErIHUFN1m8wjdh2l1zMRn_6fL"
        ),
        SmartContractInteraction(
            "Сheck-in", "EQB99O1Vlgh7BY9tzP3zPgrUSMFztaNJ12-5It09O2pH36YK", op_codes=[-3392236]
        ),
    ],
)
