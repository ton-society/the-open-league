from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
TheRoyalFortess app
"""

RoyalFortess = App(
    name="The Royal Fortess",
    analytics_key=None,
    metrics=[
        SmartContractInteraction(
            "Deposits", address="EQC7UP3tlXsrr8lOLJvTNXgY1dIxOlL7ezvOkxpdf5Ucebdz"
        )
    ]
)
