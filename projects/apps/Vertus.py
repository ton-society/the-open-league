from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Vertus app
"""

Vertus = App(
    name="Vertus",
    analytics_key="Vertus",
    url="https://t.me/Vertus_App_bot",
    metrics=[
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQARZxhi1bUv_hwYWxp_hPVZbKiAaAJKvSlK_y9q18JtIQqp",
        ),
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQD2XT3zfp0vx4CFPJf8MIJXuGtDg9SyJIGxEWaVoF-V9DEF",
        ),
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQBFEU1Yh0wuRFrkHTKq7df3oX6wH_8T0WEAzmN81Jyqdub6",
        ),
    ]
)
