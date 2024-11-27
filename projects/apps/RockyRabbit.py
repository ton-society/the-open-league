from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App
from projects.tokens.RabBitcoin import RabBitcoin

"""
Rocky Rabbit app
"""

RockyRabbit = App(
    name="Rocky Rabbit",
    analytics_key="rockyrabbit",
    url="https://t.me/rocky_rabbit_bot",
    metrics=[
        SmartContractInteraction(
            "Interaction",
            "EQATn0-JOLohp4Wi4y25-3fCpYN9QhU0J_vua2RyVO2_kFoK",
            comment_required=True,
        ),
    ],
    token=RabBitcoin,
)
