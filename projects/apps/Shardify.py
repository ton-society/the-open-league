from models.metrics.nft_transfers_to_address import NFTTransfersToAddress

from models.project import App

"""
Shardify app
"""

Shardify = App(
    name="Shardify",
    analytics_key=None,
    url='https://t.me/shardify_bot',
    metrics=[
        NFTTransfersToAddress(
            "NFT → wNOT", "EQCIXQn940RNcOk6GzSorRSiA9WZC9xUz-6lyhl6Ap6na2sh"
        ),
    ]
)
