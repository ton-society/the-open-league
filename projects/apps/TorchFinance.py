from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Torch Finance app
"""

TorchFinance = App(
    name="Torch Finance",
    analytics_key="TorchFinance",
    url="https://t.me/torch_finance_bot/torlympics",
    metrics=[
        SmartContractInteraction(
            "Deposit TON",
            "EQCaEOMOR2SRcXTVSolw--rY62ghCoCRjn4Is3bBdnqYwIVZ",
        ),
        TokenTransferFromUser(
            "Deposit Jetton",
            jetton_masters=[
                "EQDNhy-nxYFgUqzfUzImBEP67JqsyMIcyk2S5_RwNNEYku0k",  # stTON
                "EQC98_qAmNEptUtPc7W6xdHh_ZHrBUFpw5Ft_IzNU20QAJav",  # tsTON
            ],
            destinations=[
                "EQCaEOMOR2SRcXTVSolw--rY62ghCoCRjn4Is3bBdnqYwIVZ",
            ],
        ),
    ],
)
