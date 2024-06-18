from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
EdChess app
"""

EdChess = App(
    name="EdChess",
    analytics_key="EdChessGame",
    url="https://t.me/edchess_bot",
    metrics=[
        SmartContractInteraction(
            "Payment to application wallet", 
            address="EQB-YrkPdB-fYHqwDn_Wj86Vu7MHJXnlpZuNHN_MUHiXBeLa",
        )
    ]
)
