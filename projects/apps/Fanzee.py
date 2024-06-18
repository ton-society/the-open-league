from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Fanzee app
"""

Fanzee = App(
    name="Fanzee",
    analytics_key="Fanzee",
    url='https://t.me/fanzeebattlesbot',
    metrics=[
        SmartContractInteraction(
            "Deposits in TON", "EQDMN701aHQG9TvbnIqI5oEmvPN6HaTk_DBqkwTGQJWSXC_x", comment_required=True
        ),
        TokenTransferFromUser(
            "on-chain battles (FNZ or !NOT transfers), deposits in FNZ",
            jetton_masters=[
                "EQDCJL0iQHofcBBvFBHdVG233Ri2V4kCNFgfRT-gqAd3Oc86", # FNZ
                "EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT" # NOT
            ],
            destinations=[
                "EQAk7Jns6JU3fz9zeJJvMVi1C06crWGtD4H_6TVFFbcML_HS", # Staking
                "EQAXroTAyntlUD81eZ5ZUA1EWaUvTIVDx-yWl-9dPi7jwNVj", # battles
                "EQDMN701aHQG9TvbnIqI5oEmvPN6HaTk_DBqkwTGQJWSXC_x"  # battles
            ]
        )
    ]
)
