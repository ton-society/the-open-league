from models.metrics.dex_swaps import DexSwaps
from models.metrics.jetton_burn import JettonBurn
from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App
from projects.tokens.jNANO import jNANO

"""
Tonano app
"""

Tonano = App(
    name="Tonano",
    analytics_key="tonano",
    url='https://t.me/TonanoBot',
    metrics=[
        JettonBurn(
            "Tonano bridge out", jetton_masters=[
                "EQAAV0-SGQ9biuzgd5sgrnv0z_7s46bVvhQzBuWOLnSFCkhB", # jNANO-C
                "EQCOGp1GAVk51prVBw5DO8QN3lKIlUJKjXbZcl5aXgL5hkwy", # jNANO
                "EQAYgRcF2epGp3qGN_Fvz0UgQYbnchOO3dQtxt0qy_5Smc9I" # jTOL
            ]
        ),
        SmartContractInteraction(
            "Donations", "EQDc4RBidUBLRYeGhSGoNzoxBkMJCCq-o6prwZW-PboQVrMK"
        ),
        SmartContractInteraction(
            "$COFE launch", "EQCfs5XV-DPq8m8FJO3ne5DC1m9JurOOc1c_BM_zAdtBb5fB"
        ),
        SmartContractInteraction(
            "$COFE mining", "EQBk4cU_amh8w-49-NXJM0M_lNzKuFVM_Iz2r7qSirC605vG", comment_required=True
        ),
        DexSwaps(
            "Referral swaps", "EQCoLYYNH8N4q5nwatlqBRQgI5PDaEWf3glpghCZyysdENUF"
        ),
        SmartContractInteraction(
            "fomoTON (https://x.com/cofejp/status/1789310174995648527?s=46&t=K0mfb3BTzb1TuLJ_4h-SaQ)", "EQDNIDq9LETKbioifSl1hIGjxUquFWoD8XYEDc9cyvablOev", comment_regexp='fomo'
        )
    ],
    token=jNANO
)
