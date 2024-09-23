from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
NOTBITCOIN app
"""

NOTBITCOIN = App(
    name="NOTBITCOIN",
    analytics_key="notbitcoin",
    url="http://t.me/notbitco_in_bot",
    metrics=[
        SmartContractInteraction(
            "Withdraw",
            "EQB5-O2s7JwG_KXVjAH1c5JavEH8I5I67RM-QxH7KZyduLYo",
            comment_required=True,
        ),
        SmartContractInteraction(
            "Purchase",
            "EQB5-O2s7JwG_KXVjAH1c5JavEH8I5I67RM-QxH7KZyduLYo",
            op_codes=[2026481737],
        ),
    ],
)
