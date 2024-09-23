from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App
from projects.tokens.PET import PET

"""
Tongochi app
"""

Tongochi = App(
    name="Tongochi",
    analytics_key=None,
    url='https://t.me/TonGochi_bot',
    nfts=[
        "EQBHcQFym6BAxdOmU2abpTYX5ci-WG92sbjTDMC2fFzqNu8M",
        "EQBaKtgtqzI_C6SkjjkhPkXdjggnDtfXPY2Sr6p3iVVmMyIN",
        "EQDbE6ABTq1zQJZLMKOCKvIlfhx3Z6t_tbhkEm8eZ6kBjVbM",
        "EQApGxeI3NnmmSGpa0DdMfj_MXH0fC7E94nJrejYSsO-qrgk",
        "EQArhEFS4oAqBGxH8GEwUNpZBivM8moF5sEaBXxM6X3v6NAj"
    ],
    metrics=[
        NFTActivity(
            "Project's NFTs", collections=[
                "EQBHcQFym6BAxdOmU2abpTYX5ci-WG92sbjTDMC2fFzqNu8M",
                "EQBaKtgtqzI_C6SkjjkhPkXdjggnDtfXPY2Sr6p3iVVmMyIN",
                "EQDbE6ABTq1zQJZLMKOCKvIlfhx3Z6t_tbhkEm8eZ6kBjVbM",
                "EQApGxeI3NnmmSGpa0DdMfj_MXH0fC7E94nJrejYSsO-qrgk",
                "EQArhEFS4oAqBGxH8GEwUNpZBivM8moF5sEaBXxM6X3v6NAj"
            ]
        ),
        TokenTransferFromUser(
            "Staking & deposits",
            jetton_masters=[
                "EQBJOJ2eL_CUFT_0r9meoqjKUwRttC_-NUJyvWQxszVWe1WY" # PET
            ],
            destinations=[
                "EQArhEFS4oAqBGxH8GEwUNpZBivM8moF5sEaBXxM6X3v6NAj", # staking
                "EQDsQeFKUlh8iFjF_7DyUA7j0Y6kvI4CFEXiU7Gd7qQgks-7" # deposits

            ]
        ),
        SmartContractInteraction(
            "TON Deposits",
            address='EQDsQeFKUlh8iFjF_7DyUA7j0Y6kvI4CFEXiU7Gd7qQgks-7', comment_required=True,
            comment_not_equals=["Royalty"]
        )
    ],
    token=PET
)
