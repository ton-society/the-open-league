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
            "Contract calls", "EQBDnRbwoxKsjrenrNQxHtMRnwu7mu7cNxtJN2-VDD16FoDW"
        ),
        SmartContractInteraction(
            "Claim quackster", "EQCnBscEi-KGfqJ5Wk6R83yrqtmUum94SXnSDz3AOQfHGjDw"
        ),
        SmartContractInteraction(
            "Daily check-in", "EQA9xJgsYbsTjWxEcaxv8DLW3iRJtHzjwFzFAEWVxup0WH0R"
        )
    ]
)
