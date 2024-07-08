from models.metrics.gaspump_metrics import GasPumpJettonsBuys, GasPumpJettonsSellsAndUnwraps
from models.project import App

"""
GasPump app
"""

GasPump = App(
    name="GasPump",
    analytics_key="gaspump",
    url='https://t.me/gaspump_bot',
    metrics=[
        GasPumpJettonsBuys(
            "GasPump jettons buys",
            admin_addresses=["EQDM09e4e5kK0CB2vaHsmOmJtRRN-8fn-GUxNLDTjES-oJA2", "EQC24Ilm0hH8O0SUXbyfaLOhpX99E5bB1ZqSLAo6atYEybx5"]
        ),
        GasPumpJettonsSellsAndUnwraps(
            "GasPump jettons sells and unwraps",
            admin_addresses=["EQDM09e4e5kK0CB2vaHsmOmJtRRN-8fn-GUxNLDTjES-oJA2", "EQC24Ilm0hH8O0SUXbyfaLOhpX99E5bB1ZqSLAo6atYEybx5"]
        )
    ]
)
