from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App
from projects.tokens.GRAM import GRAM

"""
Gram app
"""

Gram = App(
    name="Gram",
    analytics_key=None,
    url='https://pool.gramcoin.org/',
    nfts=["EQAic3zPce496ukFDhbco28FVsKKl2WUX_iJwaL87CBxSiLQ"],
    metrics=[
        SmartContractInteraction(
            "GRAM mining", addresses=[
                "EQCfwe95AJDfKuAoP1fBtu-un1yE7Mov-9BXaFM3lrJZwqg_",
                "EQBoATvbIa9vA7y8EUQE4tlsrrt0EhSUK4mndp49V0z7Me3M",
                "EQAV3tsPXau3VJanBw4KCFaMk3l_n3sX8NHZNgICFrR-9EGE",
                "EQAR9DvLZMHo9FAVMHI1vHvL7Fi7jWgjKtUARZ2S_nopQRYz",
                "EQC10L__G2SeEeM2Lw9osGyYxhoIPqJwE-8Pe7728JcmnJzW",
                "EQDZJFkh12kw-zLGqKSGVDf1V2PRzedGZDFDcFml5_0QerST",
                "EQCiLN0gEiZqthGy-dKl4pi4kqWJWjRzR3Jv4jmPOtQHveDN",
                "EQDB8Mo9EviBkg_BxfNv6C2LO_foJRXcgEF41pmQvMvnB9Jn",
                "EQAidDzp6v4oe-vKFWvsV8MQzY-4VaeUFnGM3ImrKIJUIid9",
                "EQAFaPmLLhXveHcw3AYIGDlHbGAbfQWlH45WGf4K4D6DNZxY",
            ]
        ),
        NFTActivity(
            "Gram DNS", collections=["EQAic3zPce496ukFDhbco28FVsKKl2WUX_iJwaL87CBxSiLQ"]
        ),
        TokenTransferFromUser(
            "GRAM domains mints",
            jetton_masters=["EQC47093oX5Xhb0xuk2lCr2RhS8rj-vul61u4W2UH5ORmG_O"],
            destinations=["EQAic3zPce496ukFDhbco28FVsKKl2WUX_iJwaL87CBxSiLQ"]

        )
    ],
    token=GRAM
)
