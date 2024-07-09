from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Uniton app
"""

Uniton = App(
    name="Uniton",
    analytics_key="Uniton",
    url="https://t.me/UnitonAIBot",
    metrics=[
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQCWilCkyzHmxZZMo9z7_G85wiXlnwWMLqZAP3Lj_BC4vv7z",
        ),
        SmartContractInteraction(
            "Boost", 
            address="EQCmcNNW6_8hcwEyK46fAJiEeFkiZ4RaWsr4v8z9tohE_zwa",
        )
    ]
)
