from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
ZenCoin app
"""

ZenCoin = App(
    name="ZenCoin",
    analytics_key="theZencoin_bot",
    url="https://t.me/theZencoin_bot",
    metrics=[
        SmartContractInteraction(
            "Сheck-in", "EQAKDZF-w4PLAJcXq_RyNysXm1bepKK_OGkDJGeVVe0IlTXs", op_codes=[-926769531]
        ),
    ],
)
