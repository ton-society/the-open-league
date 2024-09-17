from models.metrics.contracts_by_code_hash import ProxyContractInteraction
from models.project import App
from projects.tokens.SOX import SOX

"""
NobbyGame app
"""

NobbyGame = App(
    name="NobbyGame",
    analytics_key="nobby_game",
    url="https://t.me/NobbyGame_bot",
    nfts=[
        "EQBZgEOY-SZWzTlg-jrLp_yPCj4r_U-jgiR2rqpXsYZgzZz1",
        "EQCoY9Slq1dNWGY3mODzS6ZixmXCY-8XiSwT1DGTW3u7iTZT",
        "EQAuvOFClTXbGGuSELiZz8tTEWOY-iyBwkUEpsWn-ZEcME4E",
        "EQBaE_70Tg9Te7jhdxVD9xPEdAdVt9W_rx1nRXeBK0-zleEZ",
        "EQAAGZm04-__vy_Hg9vpPeoYYb6QmfZuv2RxoNDrGO0s2cJg",
    ],
    metrics=[
        ProxyContractInteraction(
            "Referral payments",
            "DPYZSGR6pd6TSbTWb2A4RKXPnJB0i8g/SnXZuqu97s4=",
            op_codes=[1137169865],
        )
    ],
    token=SOX,
)
