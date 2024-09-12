from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
GH Arena app
"""

GHArena = App(
    name="GH Arena",
    analytics_key="GH_Arena",
    url="https://t.me/GHArenaBot",
    nfts=["EQBtxv9Y6zuNQDzqjBAAa2ETOoQjKlp5C5HwXXb31rh2zsVY"],
    metrics=[
        SmartContractInteraction(
            "Claiming season reward", "EQCUsXuAgsZBHR5P7DSxFbonKI0_62ptcYTv-6yWomfHihtx", comment_required=True
        ),
    ],
)
