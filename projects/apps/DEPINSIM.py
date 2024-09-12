from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
DEPINSIM app
"""

DEPINSIM = App(
    name="DEPINSIM",
    analytics_key="DepinSim",
    url="https://t.me/DepinSimBot",
    metrics=[
        SmartContractInteraction(
            "Purchase in TON",
            "EQC9jJri7_GElDmGwNuRAYnzIKzpvvLKkewn9FnNZuoB_mCp",
            comment_required=True,
        ),
        TokenTransferFromUser(
            "Purchase in Jetton",
            jetton_masters=[
                "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",  # USDT
            ],
            destinations=[
                "EQC9jJri7_GElDmGwNuRAYnzIKzpvvLKkewn9FnNZuoB_mCp",
            ],
        ),
    ],
)
