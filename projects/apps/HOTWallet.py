from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
HOT Wallet app
"""

HOTWallet = App(
    name="HOT Wallet",
    analytics_key=None,
    url="https://t.me/herewalletbot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQA4SmkTldq7Fn311uMDsvWPo_lbjamZmMZneXUcAJrJeYvm",
        ),
        SmartContractInteraction(
            "Interaction",
            "EQBxAcKP8QDDiwYolea9vTiP-O1nvP4H6Kjtx3BmsU4_klbt",
        ),
        SmartContractInteraction(
            "Interaction",
            "EQCgaC5OFAtfJjysbwP85d4Gsfgp1X-18z2S4-RIqb6z38Sk",
        ),
        SmartContractInteraction(
            "Interaction",
            "EQAvUDmCAM9Zl_i3rXeYA2n-s_uhM4rTBhzAQUeJIxEOB62i",
        ),
    ],
)
