from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
CatXWar app
"""

CatXWar = App(
    name="CatXWar",
    analytics_key="CatsXWar",
    url="https://t.me/CatsXWarBot",
    metrics=[
        SmartContractInteraction(
            "User sign-in counts", 
            address="EQAh8jHH38jcN-01nNAJjQfm-Y6sUJVXk21U3wLIA49Ef4bC"
        )
    ]
)
