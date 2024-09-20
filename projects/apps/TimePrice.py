from models.metrics.dex_swaps import DexSwaps
from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App
from projects.tokens.TIME import TIME

"""
Time Price app
"""

TimePrice = App(
    name="Time Price",
    analytics_key="Time_Price",
    url="https://t.me/Timeprice_stat_bot",
    nfts=[
        "EQBKEDSQpbnMG3qm3XVkBb15WE55lA8xlNJ5uLrS1lnrNngr",
    ],
    metrics=[
        DexSwaps(
            "Referral swaps",
            "EQCrhMJ2ZpTXE17N-VRyCEUMQphfE-5y1VtkIpmzEPm5xPex",
        ),
        DexSwaps(
            "Referral swaps",
            "EQC2fgcn74hlpvCxbVdtZ5gTVSOWHXYHVGXbqC9uB5JBQTIa",
        ),
        SmartContractInteraction(
            "SMC Interaction",
            "EQD_7n1RHphSbYh23FNvHFAIz8JgRVoOBT41BJZugpwZpkoe",
            comment_required=True,
        ),
    ],
    token=TIME,
)
