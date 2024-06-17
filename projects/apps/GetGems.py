from models.metrics.gg_collections_mint import GetGemsCollectionsMints
from models.metrics.nft_activity import NFTActivity
from models.metrics.nft_marketplace import NFTMarketplace
from models.metrics.nft_transfers_contract import NFTTransfersContractType
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App

"""
GetGems app
"""

GetGems = App(
    name="GetGems",
    analytics_key=None,
    url='https://getgems.io/',
    metrics=[
        NFTMarketplace("Marketplace sales", "EQBYTuYbLf8INxFtD8tQeNk5ZLy-nAX9ahQbG_yl1qQ-GEMS"),
        NFTMarketplace("Marketplace sales", "EQCjk1hh952vWaE9bRguFkAhDAL5jj3xj9p0uPWrFBq_GEMS"),
        NFTActivity(
            "GetGems DNS", collections=["EQDhlVq6cknyPk_SCGZUoXZRbZixNODfcBMCZ3wDfDWLFze7"]
        ),
        SmartContractInteraction(
            "GetGems DNS mints", address="EQDhlVq6cknyPk_SCGZUoXZRbZixNODfcBMCZ3wDfDWLFze7", op_codes=[1178019994]
        ),
        GetGemsCollectionsMints("Collections mints on GetGems"),
        NFTTransfersContractType("GetGems offers", contract_code_hash='y5ih9C6+oq1JHlGAOOAbyKc5J8dizVXbf5wpxhHQQUA='),
        SmartContractInteraction(
            "Absurd check-in", address="EQAQOz1tsZuWx7TfLTWeugm6ZAJQbTmSb5Xxr-2PA73js5EV"
        ),
        SmartContractInteraction(
            "Dogs breeding", address="EQBVseTUbsrVLLebSBj3tEGmzSvqjKZ9sr5P_WwErXSH0q_1", comment_required=True
        ),
        SmartContractInteraction(
            "NFT launchpads", addresses=[
                "EQCn3wEomTSkw8djmrr6_ZOu_R_XHeeDHN3Xr_Vp9gH-R1UI",
                "EQDTNVU_DU1wPNszs8tmDLh-h0sCLye4NlpTlKRa3w0yYUBI",
                "EQA_0ZJF8jERyHT3APhwqUOvGgzCqQfzhKLxh7g7HGDQp2OE",
                "EQA0UjfbEgAedksW_1__TwBZfxqd2jg1zOLDoI_7dF4iDADK",
                "EQDr7wNXb_Ce0grvp-H5lCqwzxjaB0IH6-ZnjZZxoMKwVxiC",
                "EQCUR_8mhmYxr2UFkGHE6AgHmcxpQXqSaPNbWHXY26Sp20tb",
            ], op_codes=[1994]
        ),
        SmartContractInteraction(
            'Absurd check-in', address="EQByxhbOkRKssQTSjnZOYNvl9T3IYqmDPvbGiwhaqrR4Mdbz", op_codes=[2011669209]
        )
    ]
)
