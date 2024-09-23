from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class DexSwapsRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        return f"""
        select msg_id as id, '{context.project.name}' as project, 1 as weight,
        swap_user  as user_address, ts
        from dex_swaps_local
        WHERE referral_address = '{metric.referral_address}'
        """

class DexSwapsToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        return f"""
        select tx_hash as id, '{context.project.name}' as project,
        swap_user  as user_address, ts
        from dex_swaps_local
        WHERE referral_address = '{self.to_raw(metric.referral_address)}'
        """

"""
Dex Swaps with ref address
"""
class DexSwaps(Metric):
    def __init__(self, description, referral_address):
        Metric.__init__(self, description, [DexSwapsRedoubtImpl(), DexSwapsToncenterCppImpl()])
        self.referral_address = referral_address

