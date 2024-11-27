from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
TON STATION app
"""

TONSTATION = App(
    name="TON STATION",
    analytics_key="tonstationgames",
    url="https://t.me/tonstationgames_bot",
    metrics=[
        SmartContractInteraction(
            "Check-in",
            "EQC7m1us8wg8AED2J_L8qq_mtiSSbXZuXu90q0jYqVqRiHK6",
        ),
        SmartContractInteraction(
            "One-time interaction",
            "EQCMK0ZsnOTO5d6afpYkAf7c5OeijrwV3Nb6JuVK5p1yW4Co",
        ), 
        SmartContractInteraction(
            "Daily check-in store",
            "EQCVWxdV_MvJwnbUgEPozzAgNbuYS-atK7DMEr6Dg6ubyO8O",
        ), 
        SmartContractInteraction(
            "Store",
            "EQC_7zCMsmLHRZJbylOFMljg1XYURTgMmQCv9Q-0hTVqVWIY",
        ), 
        SmartContractInteraction(
            "Daily check-in offer",
            "EQC9RwQTLrYmp2dLAHq2JjoLx1m95RzSavGH2Yuu5EB2zgB_",
        ), 
    ],
)
