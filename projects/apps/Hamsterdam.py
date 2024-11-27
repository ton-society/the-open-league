from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Hamsterdam app
"""

Hamsterdam = App(
    name="Hamsterdam",
    analytics_key="Hamsterdam",
    url="https://t.me/HamsterdamPlayBot",
    metrics=[
        SmartContractInteraction(
            "Deposit",
            "EQCfEpfNxxKMPN_r7FvGUimigqvIkcPhVqVTnCuDeN97KXft",
            comment_required=True,
        ),
        TokenTransferFromUser(
            "Stake creation",
            jetton_masters=[
                "EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT",
                "EQCvxJy4eG8hyHBFsZ7eePxrRsUQSFE_jpptRAYBmcG_DOGS",
                "EQAJ8uWd7EBqsmpSWaRdf_I-8R8-XHwh3gsNKhy-UrdrPcUo",
                "EQD-cvR0Nz6XAyRBvbhz-abTrRC6sI5tvHvvpeQraV9UAAD7",
            ],
            destinations=[
                "EQD1EGYWuqLTKSjoxTzrnqnWFnxlId2jNST0FCgZwMrQTmO_",
            ]
        ),
        SmartContractInteraction(
            "Stake withdrawal",
            "EQD1EGYWuqLTKSjoxTzrnqnWFnxlId2jNST0FCgZwMrQTmO_",
            op_codes=[-678772557],
        )
    ],
)
