from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
TheRoyalFortess app
"""

RoyalFortress = App(
    name="The Royal Fortress",
    analytics_key=None,
    metrics=[
        SmartContractInteraction(
            "Deposits", address="EQC7UP3tlXsrr8lOLJvTNXgY1dIxOlL7ezvOkxpdf5Ucebdz"
        )
    ]
)
