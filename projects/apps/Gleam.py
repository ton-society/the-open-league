from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Gleam app
"""

Gleam = App(
    name="Gleam",
    analytics_key="Gleam",
    url="https://t.me/Gleam_AquaProtocol_Bot/app",
    metrics=[
        SmartContractInteraction(
            "In-game points purchase", 
            address="EQAFZftT5VrtXl99fq7HFK0uiPwwnNKTf4CIYzH8d4RX_oDu",
            op_codes=[2019279690]
        ),
        SmartContractInteraction(
            "Completing a quest", 
            address="EQADW_UziWpTavUApnKj9ejTrGtOuIBDdIe2zxamdNkta95p",
            op_codes=[-1858389630]
        )
    ]
)
