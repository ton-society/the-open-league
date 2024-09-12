from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class TokenTransferFromUserRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        destinations = "\nor\n".join(map(lambda addr: f"jt.destination_owner  = '{addr}'", metric.destinations))
        if metric.jetton_masters and len(metric.jetton_masters) > 0:
            jetton_masters = "\nor\n".join(map(lambda addr: f"jt.jetton_master  = '{addr}'", metric.jetton_masters))
        else:
            jetton_masters = "TRUE"

        return f"""
        select jt.msg_id as id, '{context.project.name}' as project, {0.5 if metric.is_custodial else 1} as weight,
        jt.source_owner as user_address, ts
        from jetton_transfers_local jt
        WHERE (
            {destinations}
        )
        AND (
            {jetton_masters}
        )
        """


class TokenTransferFromUserToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        return f"""
select '1' as id, 'x' as project, null as address, 1 as ts
        """

"""
TEP-74 token (jetton) transfer, allows to specify the list of destinations and the list of jetton addresses.
This metric covers jetton transfer from user to smart contract
"""
class TokenTransferFromUser(Metric):
    def __init__(self, description, jetton_masters=[], destinations=[], is_custodial=False):
        Metric.__init__(self, description, [TokenTransferFromUserRedoubtImpl(), TokenTransferFromUserToncenterCppImpl()])
        assert type(jetton_masters) == list
        assert type(destinations) == list
        self.jetton_masters = jetton_masters
        self.is_custodial = is_custodial
        self.destinations = destinations

