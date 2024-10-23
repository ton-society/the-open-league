from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
Nomis app
"""

Nomis = App(
    name="Nomis",
    analytics_key="NomisApp",
    url="https://t.me/NomisAppBot",
    nfts=["EQBykWvdmoyFD2kB4BJbdrxRqyWKzSLDn-SgwNvznRfbsaKv"],
    metrics=[
        SmartContractInteraction(
            "Interaction", "EQBykWvdmoyFD2kB4BJbdrxRqyWKzSLDn-SgwNvznRfbsaKv"
        ), 
        SmartContractInteraction( 
            "Nomis Boost", 
            "EQBPIFKq_HLbqoksBqPGIMjFjTco2NH7o0ckV5Iocj_A2z-z" 
        ),
    ],
)
