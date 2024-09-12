from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class ProxyContractInteractionRedoubtImpl(RedoubtMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        if len(metric.op_codes) > 0:
            op_codes_filter = " OR ".join(map(lambda op: f"m.op = {op}", metric.op_codes))
        else:
            op_codes_filter = "TRUE"
        return f"""
        (
            with proxy_contracts as (
                select distinct(address) from account_state where code_hash = '{metric.code_hash}'
            )
            select msg_id as id, '{context.project.name}' as project, 1 as weight, source as user_address, ts
            from messages_local m
            join proxy_contracts pc on pc.address = m.destination
            where {op_codes_filter}
        )
        """

class ProxyContractInteractionToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        return f"""
select '1' as id, 'x' as project, null as address, 1 as ts
        """

"""
Interaction with a smart contract with a specific code hash
Options:
* code_hash - hash of proxy contract code
* op_codes - list of op codes (please use signed decimal notation, not hex!)
"""
class ProxyContractInteraction(Metric):
    def __init__(self, description, code_hash=None, op_codes=[]):
        Metric.__init__(self, description, [ProxyContractInteractionRedoubtImpl(), ProxyContractInteractionToncenterCppImpl()])
        self.code_hash = code_hash
        self.op_codes = op_codes
