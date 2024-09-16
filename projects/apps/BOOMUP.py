from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App
from projects.tokens import BOOM

"""
BOOM UP app
"""

BOOMUP = App(
    name="BOOM UP",
    analytics_key="boomup_game",
    url="https://t.me/Boomup_game_bot",
    metrics=[
        TokenTransferFromUser(
            "Deposit",
            jetton_masters=[
                "EQDXwweWbZtUBQIgyB34ZPCOe_PM7Par_R5Ey0hyg__yhz5f",  # BOOM
            ],
            destinations=["EQAIf0LQhvx5K-_si9rqTIKfd6zF5cvK-E-hxrgK-03-xqUL"],
        )
    ],
    token=BOOM,
)
