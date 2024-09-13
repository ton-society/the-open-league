from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Doggers app
"""

Doggers = App(
    name="Doggers",
    analytics_key="Doggers",
    url="https://t.me/doggtonbot",
    metrics=[
        SmartContractInteraction(
            "Check-in",
            "EQDyZzdx2nza-c3ML-w6JdbxgHKhtKhz6_VEJVms69qi_8ND",
            comment_required=True,
        ),
    ],
)
