from models.metrics.jetton_master_interaction import JettonMasterInteraction
from models.metrics.contracts_by_code_hash import ProxyContractInteraction
from models.metrics.token_transfer_to_jetton_master import TokenTransferToJettonMaster
from models.project import App
from projects.tokens.PUMP import PUMP


"""
Pumpers app
"""

Pumpers = App(
    name="Pumpers",
    analytics_key="pumpers",
    url="https://t.me/PumpersTGBot",
    metrics=[
        JettonMasterInteraction(
            "RequestBuy",
            admin_addresses=["EQBmZ4IuzZc5YJfAJSvXmkD_8I7qnQ5uq7N3U4MtH_N9YLNd"],
            op_codes=[431239495],
        ),
        ProxyContractInteraction(
            "Buy with UserProxy",
            code_hash="pui2fZF/DpzjMqYOvkjTOR4EDvBVtVyvhCnwRkhkkgM=",
            op_codes=[2122802415],
        ),
        TokenTransferToJettonMaster(
            "Sell",
            admin_addresses=["EQBmZ4IuzZc5YJfAJSvXmkD_8I7qnQ5uq7N3U4MtH_N9YLNd"],
        ),
    ],
    token=PUMP,
)
