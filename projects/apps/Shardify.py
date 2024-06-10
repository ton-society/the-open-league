from models.metrics.nft_activity import NFTActivity
from models.metrics.nft_transfers_to_address import NFTTransfersToAddress
from models.metrics.shardify_unwrap import ShardifyUnwrap
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Shardify app
"""

Shardify = App(
    name="Shardify",
    analytics_key=None,
    metrics=[
        NFTTransfersToAddress(
            "NFT → wNOT", "EQCIXQn940RNcOk6GzSorRSiA9WZC9xUz-6lyhl6Ap6na2sh"
        ),
        ShardifyUnwrap(
            "wNOT → NFT",
            "D2JLuV8P4sEBYC17ZjTt0fnbCVTb5WLZX7pK5SOki6k=" # TODO may be simplify...
        )
    ]
)
