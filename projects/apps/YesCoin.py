from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
YesCoin app
"""

YesCoin = App(
    name="YesCoin",
    analytics_key=None,
    metrics=[
        SmartContractInteraction(
            "Check-in", "EQCQW9JDf-W0mON_yjPLAbpdKvK49MM6RZEk8it45XO45ECC", op_codes=[-1839508102]
        )
    ]
)
