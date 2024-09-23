from models.metrics.dex_swaps import DexSwaps
from models.project import App

"""
HOT Wallet app
"""

HOTWallet = App(
    name="HOT Wallet",
    analytics_key=None,
    url="https://t.me/herewalletbot",
    metrics=[
        DexSwaps(
            "Referral swaps",
            "EQBxrkqb9sVVGBVqNJzJW9lDcKwhhgeamkBJNt1njgo_tU7s"
        ),
    ],
)
