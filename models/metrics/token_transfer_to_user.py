from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class TokenTransferToUserRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        destinations = "\nor\n".join(map(lambda addr: f"jt.source_owner  = '{addr}'", metric.sources))
        if metric.jetton_masters and len(metric.jetton_masters) > 0:
            jetton_masters = "\nor\n".join(map(lambda addr: f"jt.jetton_master  = '{addr}'", metric.jetton_masters))
        else:
            jetton_masters = "TRUE"

        if metric.initiated_by_user:
            initiator_filter = """
            exists (
                select destination from messages m where msg_id = originated_msg_id and
                destination = destination_owner -- tx chain initiated by ext message
            )
            """
        else:
            initiator_filter = "TRUE"

        return f"""
        select jt.msg_id as id, '{context.project.name}' as project, {0.5 if metric.is_custodial else 1} as weight,
        jt.destination_owner as user_address, ts
        from jetton_transfers_local jt
        WHERE (
            {destinations}
        )
        AND (
            {jetton_masters}
        ) AND (
            {initiator_filter}
        )       
        """


"""
TEP-74 token (jetton) transfer, allows to specify the list of destinations and the list of jetton addresses
This metric covers jetton transfer to user from smart contract.
- initiated_by_user flag requires that operation was initiated by the token recipient 
"""
class TokenTransferToUser(Metric):
    def __init__(self, description, jetton_masters=[], sources=[], initiated_by_user=False, is_custodial=False):
        Metric.__init__(self, description, [TokenTransferToUserRedoubtImpl()])
        assert type(jetton_masters) == list
        assert type(sources) == list
        self.jetton_masters = jetton_masters
        self.is_custodial = is_custodial
        self.sources = sources
        self.initiated_by_user = initiated_by_user

