from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Moon App app
"""

MoonApp = App(
    name="Moon App",
    analytics_key="ton1moonBot",
    url="https://t.me/ton1moonBot",
    nfts=[
        "EQAwiTMOHzki8d8acMWHbp1aRZBjRXL1T8106o8hmNDC73bS",
        "EQB4pOrnRDMLaFxR45Wq1QaMQDNdJOBw8suLCRfiGx040Y2Y",
        "EQBSm7S8Q3i-tOw01qc6EdpNquxNgy1J_bIwwKiHteJhpgIE",
    ],
    metrics=[
        SmartContractInteraction(
            "Check-in",
            "EQDolDEGlkYd3738-oqDTwLcX7LoBvpXR-WgHFI7CxMmsQuv",
            comment_required=True,
        ),
    ],
)
