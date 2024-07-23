from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
TypoCurator app
"""

TypoCurator = App(
    name="TypoCurator",
    analytics_key="TypoCurator",
    url="https://www.typox.ai/",
    metrics=[
        SmartContractInteraction(
            "Withdraw", 
            address="EQBk6_OV_6Kgg2_-nkI_j-3-xxOrOWiH9B5u9fwT1z_vlwFY"
        ),
        SmartContractInteraction(
            "SBT", 
            address="EQDsA8rP8HUmB0QppNqFKwkaTSP6_zbxzOY2JGlxBOeUYNxk"
        ),
        TokenTransferFromUser(
            "Deposit",
            jetton_masters=[
                "EQD9G51RpADBGVaojKpV-xNGJy3Kr9rkEHxtVXcRvoitg3vf"  # TPX
            ],
            destinations=[
                "EQBMUtlHZ-8FbWlfdEc5DN2r-g47cT4k3W_cep40c5JyUpEJ"
            ]
        )
    ]
)
