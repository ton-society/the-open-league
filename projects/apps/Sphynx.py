from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Sphynx app
"""

Sphynx = App(
    name="Sphynx",
    analytics_key="Sphynx",
    url="https://sphynx.meme/",
    metrics=[
        SmartContractInteraction(
            "Daily Check-In, In-App Purchase with Affiliate Feature", 
            address="EQAuYz5NHwEUyKW8A-6AGyWmn-DNJ3OK5giIR1I4J7g6FTh6",
            op_codes=[-871565262, -183263021]
        )
    ]
)
