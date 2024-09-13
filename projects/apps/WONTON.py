from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
WONTON app
"""

WONTON = App(
    name="WONTON",
    analytics_key="WONTON",
    url="https://t.me/WontonOrgBot",
    metrics=[
        SmartContractInteraction(
            "Deposit", "EQD_QUnVTBzwG-8GCkqnQ4xiWxU0oPZn9Pon_rq0MZVdIBuf", op_codes=[-1552920267]
        ),
        SmartContractInteraction(
            "Withdraw", "EQD_QUnVTBzwG-8GCkqnQ4xiWxU0oPZn9Pon_rq0MZVdIBuf", op_codes=[1076884676]
        ),
    ],
)
