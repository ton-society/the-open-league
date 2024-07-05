from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Catizen app - https://catizen.ai/
"""

Catizen = App(
    name="Catizen",
    analytics_key="catizen",
    url='https://t.me/catizenbot',
    prizes=False,
    metrics=[
        SmartContractInteraction(
            "Airdop claim", "EQAMl6BVegC0IOZPLhLzWBHCnK4iO4G5eNu4qn_NKQnoISvm"
        ),
        SmartContractInteraction(
            "Boost claim", "EQChB2eMoFG4ThuEsZ6ehlBPKJXOjNxlR5B7qKZNGIv256Da"
        )
    ]
)
