from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
PiggyPiggy app
"""

PiggyPiggy = App(
    name="PiggyPiggy",
    analytics_key="PiggyPiggy",
    url="https://t.me/PiggyPiggyofficialbot",
    metrics=[
        SmartContractInteraction(
            "Сheck-in", "EQANGeTSaKa2G3S3oB3yE0Be44ISWsICirzCbTyxtuv3dQQ4", op_codes=[-1874432775]
        ),
    ],
)
