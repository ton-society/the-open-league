from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
MoneyGardenAi app
"""

MoneyGardenAI = App(
    name="MONEY GARDEN AI",
    analytics_key="MoneyGardenAI",
    url='https://t.me/moneygardenaibot',
    metrics=[
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQCiY6qFHFtYtUt4pmggppA2V7OzZPmM2M7yKhD269txqcX-",
        )
    ]
)
