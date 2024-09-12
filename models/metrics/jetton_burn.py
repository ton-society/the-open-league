from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class JettonBurnRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        jetton_masters = "\nor\n".join(map(lambda addr: f"jetton_master  = '{addr}'", metric.jetton_masters))

        return f"""
        select msg_id as id, '{context.project.name}' as project, 1 as weight, user_address, ts
        from jetton_burn_local
        WHERE {jetton_masters}
        """

class JettonBurnToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        return f"""
select '1' as id, 'x' as project, null as address, 1 as ts
        """

"""
TEP-74 token (jetton) burn
"""
class JettonBurn(Metric):
    def __init__(self, description, jetton_masters=[]):
        assert type(jetton_masters) == list
        Metric.__init__(self, description, [JettonBurnRedoubtImpl(), JettonBurnToncenterCppImpl()])
        self.jetton_masters = jetton_masters

