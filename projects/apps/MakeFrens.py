from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Make Frens app
"""

MakeFrens = App(
    name="Make Frens",
    analytics_key="Make_Frens",
    url="https://t.me/MakeFrens_Bot",
    metrics=[
        SmartContractInteraction(
            "Tickets Purchase",
            "EQCbU_4fv1UBUUK5MrBBr8W3RG04gI5qKlC1kR9jX6oeo-lh",
            op_codes=[-1804953418]
        ),
        SmartContractInteraction(
            "Pay-per-task",
            "EQDF_RuRayVoMsDTdq8_zx2aDIMqFvuHdWZ6kg2hxA1jH5Ai",
            op_codes=[-1804953418]
        ),
    ],
)
