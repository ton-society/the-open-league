from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
TonGifts app
"""

TonGifts = App(
    name="TonGifts",
    analytics_key="TonGifts",
    url="https://t.me/GetTonGifts_Bot",
    metrics=[
        SmartContractInteraction(
            "Deposit TON, Withdraw", 
            address="EQAutMVU3M9MY6SPTRHG74VdJlpY-B3HVttCPY2dd8BOrxME"
        ),
        TokenTransferFromUser(
            "Deposit jettons",
            jetton_masters=[
                "EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs",  # USDT
                "EQAvlWFDxGF2lXm67y4yzC17wYKD9A0guwPkMs1gOsM__NOT",  # NOT
                "EQCp_qh6J4mdZ0Vy7_C-WELqBlMLs2fvrSKX1JMgcJ56UlRf",  # MSW
                "EQC0KYVZpwR-dTkPwVRqagH2D31he931R7oUbPIBo_77F97K",  # TONG
                "EQCvaf0JMrv6BOvPpAgee08uQM_uRpUd__fhA7Nm8twzvbE_",  # UP
            ],
            destinations=[
                "EQAutMVU3M9MY6SPTRHG74VdJlpY-B3HVttCPY2dd8BOrxME"
            ]
        )
    ]
)
