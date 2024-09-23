from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
QuackQuack app
"""

QuackQuack = App(
    name="QuackQuack",
    analytics_key="QuackQuack_TON",
    url='https://t.me/quackquack_game_bot',
    metrics=[
        SmartContractInteraction(
            "Deposits", "EQDDo8EnHzcMf_c-WKBEuoJjYqK__APFlq8fe53BoI4cpPJF"
        ),
        SmartContractInteraction(
            "Claim Referral Reward", "EQBDnRbwoxKsjrenrNQxHtMRnwu7mu7cNxtJN2-VDD16FoDW"
        ),
        SmartContractInteraction(
            "Claim quackster", "EQDCR0XQ0qNQJNjITRpo59mFsP0pjx81ImtXx92mJBnIc7m4"
        ),
        SmartContractInteraction(
            "Daily check-in", "EQA32il_GNZGw-T4LrI_6rGMDbTvC_BAIJRnp1sJMxFoReG9"
        ),
        SmartContractInteraction(
            "Claim Weekly Leaderboad Reward", "EQAB5kQnWHG6cVNfVUeBYsaDPyXxeF7-rHDDku7VU16a0qI3"
        )
    ]
)
