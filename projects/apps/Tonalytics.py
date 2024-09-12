from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Tonalytics app
"""

Tonalytics = App(
    name="Tonalytics",
    analytics_key="Tonalytics",
    url="https://t.me/tonalytics_bot",
    metrics=[
        SmartContractInteraction(
            "Сlaim", "EQDzbgNWF1CRTI8bSbGYyEtK9io4b2rCIjH_0H75Zk9DDgsv", comment_required=True
        ),
    ],
)
