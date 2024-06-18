from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
TonMap app
"""

TonMap = App(
    name="TonMap",
    analytics_key="tonmap",
    url='https://tonmap.app/',
    metrics=[
        SmartContractInteraction(
            "SBT mint", address="EQBQjoanL6qrduDIIsLw99BNpmfDiYi4gLq3YbQppUlVRDWb",
            op_codes=[993321253]
        )
    ]
)
