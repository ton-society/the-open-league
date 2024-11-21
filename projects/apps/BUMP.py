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
            "EQA1ncIYvWqZ8Lba4diqFqbZ5hY0OL2QnkE3tIULrmFnEOEz" 
        ), 
    ],
)
