from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Hipo Gang app
"""

HipoGang = App(
    name="Hipo Gang",
    analytics_key="HipoGang",
    url="https://t.me/HipoGangBot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQCLyZHP4Xe8fpchQz76O-_RmUhaVc_9BAoGyJrwJrcbz2eZ",
            op_codes=[1027039654],
        ),
    ],
)
