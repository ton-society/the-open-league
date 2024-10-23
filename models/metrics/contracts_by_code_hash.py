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
        if len(metric.op_codes) > 0:
            op_codes_filter = " or ".join(map(lambda op: f"m.opcode = {op}", metric.op_codes))
        else:
            op_codes_filter = "TRUE"
        return f"""
        (
            with proxy_contracts as (
                select distinct(account) from latest_account_states 
                where code_hash = '{metric.code_hash}' and timestamp > {context.season.start_time}
            )
            select m.tx_hash as id, '{context.project.name}' as project, m.source as user_address, m.created_at as ts 
            from messages m
            join proxy_contracts pc on pc.account = m.destination
            join transactions t on m.tx_hash = t.hash
            where t.compute_exit_code = 0 and t.action_result_code = 0
            and m.direction = 'in'
            and m.created_at >= {context.season.start_time}::integer
            and m.created_at < {context.season.end_time}::integer
            and {op_codes_filter}
        )
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
