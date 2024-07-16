from models.metrics.pumpers_metrics import JettonMasterInteraction, ProxyContractInteraction, TokenTransferToJettonMaster
from models.project import App

"""
Pumpers app
"""

Pumpers = App(
    name="Pumpers",
    analytics_key=None,
    url="https://pumpers.tg/",
    metrics=[
        JettonMasterInteraction(
            admin_addresses=["EQBmZ4IuzZc5YJfAJSvXmkD_8I7qnQ5uq7N3U4MtH_N9YLNd"],
            op_codes=[431239495],
        ),
        ProxyContractInteraction(
            code_hash="pui2fZF/DpzjMqYOvkjTOR4EDvBVtVyvhCnwRkhkkgM=",
            op_codes=[2122802415],
        ),
        TokenTransferToJettonMaster(
            admin_addresses=["EQBmZ4IuzZc5YJfAJSvXmkD_8I7qnQ5uq7N3U4MtH_N9YLNd"],
        ),
    ],
)
