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
            "Memewars",
            "EQAitPEyRsbqngxWUaP8_XZJh1Ro-Ez2f54Lp4o97oHUY78G",
            op_codes=[133295436],
        ),
        SmartContractInteraction(
            "OpenLeague",
            "EQCSuEcF5GA6Dh4cu_6YdUOYiRDKSBsyDrJRY0Gt4Ics55to",
            op_codes=[-1960889654],
        ),
        SmartContractInteraction(
            "Tickets",
            "EQCfn2sUM5jcrQvmdGAILYs-vulCi_jvQyIURDU0zZSYFAV3",
        ),
    ],
)
