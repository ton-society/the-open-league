from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
CatGoldMiner app
"""

CatGoldMiner = App(
    name="CAT GOLD MINER",
    analytics_key="cat-gold-miner",
    url="https://t.me/catgoldminerbot",
    metrics=[
        SmartContractInteraction(
            "Daily Check-in", 
            address="EQBg_0I3h4L7f1ca_tY30VUTEilVS0d6QAx8IcwGjIjLZTLr",
        ),
        SmartContractInteraction(
            "In-app purchasing", 
            address="EQCHoSb0kxasrZ-XhGdQ4vQz-ZEGQuX1Pzq-HYiWQi8-FMpy",
        ), SmartContractInteraction(
            "Bitget Wallet Check-in", 
            address="EQCPiDCGwdttxcC0Hl7ZFi8oi2UY-T3f0D4JEYikEFJXTydY",
        ),
        SmartContractInteraction(
            "OKX Wallet Check-in", 
            address="EQAZXOXkSGTCwYUfGdyug87uzenlbDpTcvmJoL8FQgsLbz1L",
        )
    ]
)
