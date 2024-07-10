from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Gleam app
"""

Gleam = App(
    name="Gleam bot - platform for Crypto projects",
    analytics_key="Gleam",
    url="https://t.me/GleamRewardsBot",
    metrics=[
        SmartContractInteraction(
            "Payment", 
            address="EQAaP62gcmar9uRh0AkIP9wrABT6dWHLet4_RmVrbwNRlrpJ",
            op_codes=[-284173732]
        )
    ]
)
