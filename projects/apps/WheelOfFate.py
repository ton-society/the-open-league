from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
WheelOfFate app
"""

WheelOfFate = App(
    name="Wheel of Fate",
    analytics_key="WheelofFate",
    url="https://www.wheeloffate.xyz/",
    metrics=[
        SmartContractInteraction(
            "Check-In", 
            address="EQBeY0eQVUR5PCUEdrnzqGF3Yd_QT6js-JCvG1dFOyTzyuW_"
        )
    ]
)
