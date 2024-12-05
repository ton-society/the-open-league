from models.project import DeFi, Correction

Delea = DeFi(
    name="Delea",
    defillama_slug="delea",
    url="https://delea.finance/",
    corrections=[
        Correction(
            value_usd=47205,
            tx_hash="I0T2Cnb/JD09RndN360sKbLQm1eSUeSLnjkt66Gn/RM=",
            description="Inintial liquidity 7001.2126 tsTON at 29.11.2024, 17:26:34",
        )
    ],
)
