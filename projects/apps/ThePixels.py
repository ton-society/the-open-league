from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
The Pixels app
"""

ThePixels = App(
    name="The Pixels",
    analytics_key="the_pixels",
    metrics=[
        SmartContractInteraction(
            "Deposits", "EQAbRnBFsHIJmk2HmY8PD91YRHCNXNuL8N8z2KmWDVZYfFLK",
            comment_required=True
        ),
        NFTActivity(
            "NFT activity", collections=["EQDPcfRFZ9EhPFT0l3K-EdlE_s7kSXboJ2GzNPLD2IJ2rZdq"]
        )
    ]
)
