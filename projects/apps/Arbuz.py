from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Arbuz app
"""

Arbuz = App(
    name="Arbuz",
    analytics_key="ClickARBUZ",
    metrics=[
        SmartContractInteraction(
            "Clicker actions", "EQCaFoHe_hgwwtj3n5gjUsmGcxHA0X_-q2mZTxyzmvbWnEtC"
        ),
        SmartContractInteraction(
            "Arbuz claim", "EQAnhNV-BnPRwfbJUOrNqnYs8YZ31sk1YAvhYSGLqfvIPEYE"
        ),
        SmartContractInteraction(
            "Arbuz lottery", "EQDughgQWkIXBSQRMef7ma-q6cEWu-T4P5-2mluj9Nxn1jQJ"
        )
    ]
)
