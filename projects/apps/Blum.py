from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Blum app
"""

Blum = App(
    name="Blum",
    analytics_key="blum_data_prod",
    url="https://t.me/BlumCryptoBot",
    metrics=[
        SmartContractInteraction(
            "Interaction_1",
            "EQA9nNvUSLAebJxzhHv5sxMWK_RXrxk4MYXR39JMbqvrc040",
            comment_required=True,
        ),
        SmartContractInteraction(
            "Interaction_2",
            "EQCEBX20fDRsi4nN953ZhvgRlTvmRD9YDWhZF4Sptly-BN5l",
            op_codes=[-676638911],
        ),
    ],
)
