from models.metrics.nft_activity import NFTActivity
from models.metrics.smc_interaction import SmartContractInteraction
from models.metrics.token_transfer_from_user import TokenTransferFromUser
from models.project import App
from projects.tokens.UP import UP

"""
TonUp app
"""

TonUP = App(
    name="TonUP",
    analytics_key=None,
    url='https://tonup.io/',
    metrics=[
        SmartContractInteraction(
            "Accept of ToS", "EQCvp_7oqAiq12G8Q5PtE0B3OV_yGk1MuTlqurKxFDGxfZ3r", comment_required=True
        ),
        SmartContractInteraction(
            "Updated ToS + UP refund", "EQDPNq_v_rCljQzrueWeIxACBVgWlJr0qtXwaZSipMRIj7pQ", comment_required=True
        ),
        TokenTransferFromUser(
            "Staking",
            jetton_masters=[
                "EQCvaf0JMrv6BOvPpAgee08uQM_uRpUd__fhA7Nm8twzvbE_" # UP
            ],
            destinations=[
                "EQBk04plpd2eNkCqREyY7XFfSp2Mpwm10FLQcGBq6U5mICCR", # UP
                "EQAxN5aREN_WF-He1uKeQsalDxobF3kz2u-5U69x_RAzK3sQ", # UP

            ]
        )
    ],
    token=UP
)
