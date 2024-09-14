from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Chick Coop app
"""

ChickCoop = App(
    name="Chick Coop",
    analytics_key="Chickcoop",
    url='https://t.me/chickcoopofficial_bot',
    metrics=[
        SmartContractInteraction(
            "Shop/Buying Gem, Lucky Wheel and Check-in",
            addresses=[
                "EQCkc4zcv43qW8_0D-FD3Br-fxvA2IoQHCSg0o3cguyQ8Nh9",
                "EQAOsRZKTrMe8ZTtwxxrAC8P84zgmYMF5YML0_NpL0jDrJRq",
                "EQBUwiwJ5Wczc5QgOo6MKL-XwSaC9z0a46abdLWqRKb5yUt6",
                "EQDd29ae4JYnoWAo9eFC4B_PJ0_eYoGaG1KAC3F-So-zJBAE"
            ],
            comment_required=True
        )
    ]
)
