from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
TopPunks app
"""

TopPunks = App(
    name="TopPunks",
    analytics_key=None,
    metrics=[
        SmartContractInteraction(
            "@cubesonthewater_bot", "EQCtEy4bAxYrDZLetcP9wyAKL3MkgMxDoe_1BxLeo-1B9F2A", comment_required=True
        ),
        SmartContractInteraction(
            "cubes on-chain claim", "EQB7isY1M7reJmnqW6bhXcwfBlyXb5TWVa6gRE_l1CQE_oEE", comment_required=True
        )
    ]
)
