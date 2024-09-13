from models.metrics.jetton_burn import JettonBurn
from models.project import App
from projects.tokens.TOWER import TOWER

"""
Crazy Rush Heroes app
"""

CrazyRushHeroes = App(
    name="Crazy Rush Heroes",
    analytics_key="Crazy_Rush_Heroes",
    url="https://t.me/crazyrushheroesalphabot",
    metrics=[
        JettonBurn(
            "Burn",
            jetton_masters=[
                "EQC47YfVLWo-U_z7s6iEOkYAAEKF_C0-gBiB8KJL6s5m4JOP",  # jTOWER
            ],
        ),
    ],
    token=TOWER,
)
