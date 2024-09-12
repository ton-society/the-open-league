from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Mine2Mine app
"""

Mine2Mine = App(
    name="Mine2Mine",
    analytics_key="Mine2Mine",
    url="https://t.me/mine2mine_bot",
    metrics=[
        TokenTransferFromUser(
            "Deposit",
            jetton_masters=[
                "EQCILWMtTu_ShFu0WPZnZx9SfCX70dTypBESubKMZUPQOd53"  # GPU
            ],
            destinations=[
                "EQBxr1xLYOL2WI3meenZgEN6ZMRUtrvo3Qn8XFz6mhpnvz7G"
            ]
        )
    ]
)
