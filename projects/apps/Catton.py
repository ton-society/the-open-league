from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
Catton app - https://catton.tech/
"""

Catton = App(
    name="Catton",
    analytics_key="catton",
    url='https://t.me/CattonAiBot',
    prizes=False,
    metrics=[
        SmartContractInteraction(
            "Game Check-in",
            "UQCvTdbpClJR7OsmWttF7D7L0Wd8qU4lVNRJUrIHprORdD9v",
        ),
        SmartContractInteraction(
            "Game Purchase",
            "UQDr2S_IC2Aeyw3EVmqBPffu7OWJZSItzCFaFcmOc10yUNHa",
        ), 
        SmartContractInteraction(
            "Game Purchase 1",
            "UQAPP3aEmdcOEUKAfCxceJScEJHA3K85RQXF3qxUo2XBCEzI",
        ), 
        SmartContractInteraction(
            "Game Purchase 2",
            "UQB6_nqdAOtxrtbbG2dTt7hw8tcpJrkLIooMg0e63tPqIY0L",
        ), 
        SmartContractInteraction(
            "Game Purchase 3",
            "UQBPb6OrV2meLFdIGpFU5rzuC476lGKwrV45uyTDTsjPYJCF",
        ),
        SmartContractInteraction(
            "Game Purchase 4",
            "UQCIJbQRsrVX0CIRR1nzb1pckdN-9kGO_kEUEO2IwDlwUjjt",
        ),
        SmartContractInteraction(
            "Game Purchase 5",
            "UQBGx-6Z-OOgyjkqsQNFwe_HV4uy6cw_FADtAn604QZEAS3U",
        ),
        SmartContractInteraction(
            "Game Purchase 6",
            "UQA0PLjKBXFkRkaWx1wc01jpFB8Ok2jtPwQzdVpU-f4H3XJl",
        ),
        SmartContractInteraction(
            "Game Purchase 7",
            "UQBAx-OPWIiUaBtq5mBvS-f_RLbyPOKV0cma5mJ1rLCPttaq",
        ),
        SmartContractInteraction(
            "Game Purchase 8",
            "UQCYGkZC5uo49UhDUIOU_bYXmxS5j_fV6VSvHd_0MCEnXfq7",
        ),
        SmartContractInteraction(
            "Game Purchase 9",
            "UQDZfMuW_5sXSVmhH33gwFTLcBwcoDSx7FF6pToePKWAji3I",
        ), 
        TokenTransferFromUser(
            "Token transfer",
            jetton_masters=[
                "EQCftEnOj7Q9D2gscTwB2dg1fHzQ1KSd1k3VhZJpkBdKTrX7", # ctUSD
            ],
            destinations=[
                "UQCvTdbpClJR7OsmWttF7D7L0Wd8qU4lVNRJUrIHprORdD9v", 
                "UQDr2S_IC2Aeyw3EVmqBPffu7OWJZSItzCFaFcmOc10yUNHa", 
                "UQAPP3aEmdcOEUKAfCxceJScEJHA3K85RQXF3qxUo2XBCEzI", 
                "UQB6_nqdAOtxrtbbG2dTt7hw8tcpJrkLIooMg0e63tPqIY0L", 
                "UQBPb6OrV2meLFdIGpFU5rzuC476lGKwrV45uyTDTsjPYJCF", 
                "UQCIJbQRsrVX0CIRR1nzb1pckdN-9kGO_kEUEO2IwDlwUjjt", 
                "UQBGx-6Z-OOgyjkqsQNFwe_HV4uy6cw_FADtAn604QZEAS3U", 
                "UQA0PLjKBXFkRkaWx1wc01jpFB8Ok2jtPwQzdVpU-f4H3XJl", 
                "UQBAx-OPWIiUaBtq5mBvS-f_RLbyPOKV0cma5mJ1rLCPttaq", 
                "UQCYGkZC5uo49UhDUIOU_bYXmxS5j_fV6VSvHd_0MCEnXfq7", 
                "UQDZfMuW_5sXSVmhH33gwFTLcBwcoDSx7FF6pToePKWAji3I"
                ]
        ),
    ]
)
