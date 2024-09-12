from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
MemeTv app
"""

MemeTv = App(
    name="MemeTv",
    analytics_key="MemeTv",
    url="https://t.me/TheMemeTvBot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQCHiGNkhPqwgDkYp-ZqAKMKqAf4k9-_Z1_IbNb-L7OBFOpr",
            op_codes=[-564733746],
        ),
    ],
)
