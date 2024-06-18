from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
MomoAI app
"""

MomoAI = App(
    name="MomoAI",
    analytics_key="Momoai",
    url="https://t.me/MomoAI_bot",
    metrics=[
        SmartContractInteraction(
            "Users who check in get hammers", 
            address="EQBH3nwV0DE1Jn2esUMQ-7Qd8DLzLNxTZTkncdP6jsL0QqCk",
        )
    ]
)
