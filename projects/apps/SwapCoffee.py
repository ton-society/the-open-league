from models.metrics.dex_swaps import DexSwaps
from models.project import App

"""
Swap.Coffee app
"""

SwapCoffee = App(
    name="swap.coffee",
    analytics_key="swapcoffee",
    url='https://t.me/swapcoffeebot',
    metrics=[
        DexSwaps(
            "Referral swaps", "EQCNTO0Nh0Z7QNyRW1BLWfk08f2dAOw4izrx9sO6OUPg4GfQ"
        )
    ]
)
