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
        SmartContractInteraction(
            "Daily Check-in", "EQAr17Jj72_h8Wier6zl7n8hB5l2RP7R00VdvmWoTCWv-gf6", op_codes=[-926769531, -1351283404]
        ),
        SmartContractInteraction(
        "In-app purchasing", "UQDZMUeSS-OSWCSCsesv8gZwVe_8lpfcq_lIl-B4MzGHLRg9"
        ),
    ],
)
