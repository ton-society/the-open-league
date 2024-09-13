from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
SquidTG app
"""

SquidTG = App(
    name="SquidTG",
    analytics_key="SquidTG",
    url='https://t.me/squidtg_bot',
    metrics=[
        SmartContractInteraction(
            "Contract call",
            address='EQCqNjAPkigLdS5gxHiHitWuzF3ZN-gX7MlX4Qfy2cGS3FWx',
            op_codes=[0x5bc58ae8, 0x768b4d10]
        ),
        SmartContractInteraction(
            "Inscription",
            address='EQCqNjAPkigLdS5gxHiHitWuzF3ZN-gX7MlX4Qfy2cGS3FWx',
            comment_regexp='%"ton-squid","op":"%'
        )
    ]
)
