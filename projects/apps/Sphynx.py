from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Sphynx app - https://sphynx.meme/
"""

Sphynx = App(
    name="Sphynx",
    analytics_key="Sphynx",
    url='https://t.me/sphynxmeme_bot',
    metrics=[
        SmartContractInteraction(
            "CheckIn", 
            addresses=["EQAuYz5NHwEUyKW8A-6AGyWmn-DNJ3OK5giIR1I4J7g6FTh6", "EQCYEVNooR5nowfTPrzx86iOCVeIuAEAGpyPJ3qwjTMXlF3U"],
            op_codes=[3423402034]
        ),
        SmartContractInteraction(
            "Purchase", 
            addresses=["EQAuYz5NHwEUyKW8A-6AGyWmn-DNJ3OK5giIR1I4J7g6FTh6", "EQCYEVNooR5nowfTPrzx86iOCVeIuAEAGpyPJ3qwjTMXlF3U"],
            op_codes=[4111704275]
        ),
        SmartContractInteraction(
            "RewardPool", 
            address="EQAuYz5NHwEUyKW8A-6AGyWmn-DNJ3OK5giIR1I4J7g6FTh6",
            op_codes=[52516493]
        )
    ]
)
