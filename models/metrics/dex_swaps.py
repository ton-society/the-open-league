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
select '1' as id, 'x' as project, null as address, 1 as ts
        """

"""
Dex Swaps with ref address
"""
class DexSwaps(Metric):
    def __init__(self, description, referral_address):
        Metric.__init__(self, description, [DexSwapsRedoubtImpl(), DexSwapsToncenterCppImpl()])
        self.referral_address = referral_address

