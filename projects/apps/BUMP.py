from models.metrics.smc_interaction import SmartContractInteraction
from models.project import App

"""
BUMP app
"""

BUMP = App(
    name="BUMP",
    analytics_key="Bump333",
    url="https://t.me/MMproBump_bot",
    nfts=[
        "EQC5XhGLN5wkEQcifzsiyOpPvDfAqLBzQwsfEEZVRS7LAxGJ",
        "EQCLxOtUQ7ouyNdqnzxcGuChtqxcbLKqxRsRmUKsQZnjwhDb",
        "EQDCU3jFPifA0MoptBDqyS4Td8TKuNN4Mw1N-AW_VGHKzzFK",
        "EQCv9ZPdQ9LQrnlWbgQ7btD5qgyzi1uWqb9trgNmdSL1ei5l",
        "EQD1NhcBmbVgNYFRMtlSDVdWcwQTmvV4YNkFSydD3FaOPQpw",
    ],
    metrics=[ 
        SmartContractInteraction( 
            "Interaction 1", 
            "EQCwF7-OQiHBxKePiBFOAWwzHDTFHkJR9likOqTYFQc08OmS", 
            op_codes=[74989363, 1997904914], 
        ), 
        SmartContractInteraction( 
            "Interaction 2", 
            "EQCms5awEaWuApGPY3zptU4QEDW_IkMKeTFZuEHBTie9sYWF" 
        ), 
        SmartContractInteraction( 
            "Interaction 3", 
            "EQCiqaHaScaQFjX1kwTDx5KHROVPt54cms2rYHBm1Ug6E19e" 
        ), 
        SmartContractInteraction( 
            "Interaction 4", 
            "EQAJ-QU4xFrQRr1JCtQS7zAgCOvVDl5tkBvgwbAGOGiRd9MO" 
        ), 
    ],
)
