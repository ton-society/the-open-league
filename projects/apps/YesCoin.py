from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
YesCoin app
"""

YesCoin = App(
    name="YesCoin",
    analytics_key="Yescoin",
    url='https://t.me/theYescoin_bot',
    metrics=[
        SmartContractInteraction(
            "Check-in", "EQCQW9JDf-W0mON_yjPLAbpdKvK49MM6RZEk8it45XO45ECC", op_codes=[-1839508102]
        ),
        SmartContractInteraction(
            "Boost claim", "EQD4QiIKQvdTwJTXQ22ZrmQOpOFl4S1e4s5oNQweFHaTgVGZ"
        )
    ]
)
