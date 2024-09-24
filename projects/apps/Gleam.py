from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Gleam app
"""

Gleam = App(
    name="Gleam bot",
    analytics_key="Gleam",
    url="https://t.me/GleamRewardsBot",
    metrics=[
        SmartContractInteraction(
            "Payment",
            address="EQAaP62gcmar9uRh0AkIP9wrABT6dWHLet4_RmVrbwNRlrpJ",
            op_codes=[-284173732],
        ),
        SmartContractInteraction(
            "TOL quest",
            address="EQAy0G_D3ma7BLJifaoNwR08kACx3KUfJaneznVKvWCF0RS8",
            comment_required=True,
        ),
    ],
)
