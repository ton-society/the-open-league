from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App
from projects.tokens.PUNK import PUNK

"""
TonPunks app
"""

TonPunks = App(
    name="TON Punks",
    analytics_key="TONPunks",
    url='https://t.me/TonPunksBot',
    nfts=["EQAo92DYMokxghKcq-CkCGSk_MgXY5Fo1SPW20gkvZl75iCN"],
    metrics=[
        SmartContractInteraction(
            "@cubesonthewater_bot", "EQCtEy4bAxYrDZLetcP9wyAKL3MkgMxDoe_1BxLeo-1B9F2A", comment_required=True
        ),
        SmartContractInteraction(
            "cubes on-chain claim", "EQB7isY1M7reJmnqW6bhXcwfBlyXb5TWVa6gRE_l1CQE_oEE", comment_required=True
        ),
        NFTActivity(
            "NFT activity", collections=["EQAo92DYMokxghKcq-CkCGSk_MgXY5Fo1SPW20gkvZl75iCN"]
        )
    ],
    token=PUNK,
)
