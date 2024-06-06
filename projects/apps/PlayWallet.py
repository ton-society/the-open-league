from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
PlayWallet app
"""

PlayWallet = App(
    name="PlayWallet",
    analytics_key="PlayWallet",
    metrics=[
        SmartContractInteraction(
            "ByBit deposits with memo", "EQDD8dqOzaj4zUK6ziJOo_G2lx6qf1TEktTRkFJ7T1c_fPQb", comment_regexp='10095754'
        )
    ]
)
