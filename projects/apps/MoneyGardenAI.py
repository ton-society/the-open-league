from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
MoneyGardenAi app
"""

MoneyGardenAI = App(
    name="MONEY GARDEN AI",
    analytics_key="moneygardenai",
    url='https://www.moneygarden.ai/',
    metrics=[
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQCjSrNwSn6lTluhWSOTmnA6O1mvz89LIt7e1rynFwZwYhUv",
        )
    ]
)
