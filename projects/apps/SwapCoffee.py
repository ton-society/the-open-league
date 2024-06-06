from models.metrics.dex_swaps import DexSwaps
from models.metrics.inscriptions import Inscriptions
from models.metrics.jetton_burn import JettonBurn
from models.metrics.jetton_mint import JettonMint
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.metrics.token_transfer_to_user import TokenTransferToUser
from models.metrics.ton20_sales import Ton20Sales
from models.project import App

"""
Swap.Coffee app
"""

SwapCoffee = App(
    name="swap.coffee",
    analytics_key=None,
    metrics=[
        DexSwaps(
            "Referral swaps", "EQCNTO0Nh0Z7QNyRW1BLWfk08f2dAOw4izrx9sO6OUPg4GfQ"
        )
    ]
)
