from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class JettonMasterInteractionRedoubtImpl(RedoubtMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        if len(metric.admin_addresses) > 0:
            admin_addresses_filter = " OR ".join(
                map(lambda addr: f"jm.admin_address = '{addr}'", metric.admin_addresses)
            )
        else:
            admin_addresses_filter = "FALSE"
        if len(metric.op_codes) > 0:
            op_codes_filter = " OR ".join(map(lambda op: f"m.op = {op}", metric.op_codes))
        else:
            op_codes_filter = "TRUE"

        return f"""
        (
            with jetton_masters as (
                select jm.address as jetton_master_address from jetton_master jm
                where {admin_addresses_filter}
            )
            select
                m.msg_id as id,
                '{context.project.name}' as project,
                1 as weight,
                m.source as user_address, ts
            from messages_local m
            join jetton_masters jm on m.destination = jm.jetton_master_address
            where {op_codes_filter}
        )
        """

class JettonMasterInteractionToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        if len(metric.admin_addresses) > 0:
            admin_addresses_filter = " OR ".join(
                map(lambda addr: f"jm.admin_address = '{self.to_raw(addr)}'", metric.admin_addresses)
            )
        else:
            admin_addresses_filter = "FALSE"
        if len(metric.op_codes) > 0:
            op_codes_filter = " OR ".join(map(lambda op: f"m.opcode = {op}", metric.op_codes))
        else:
            op_codes_filter = "TRUE"

        return f"""
        (
            with j_masters as (
                select jm.address as jetton_master_address from jetton_masters jm
                where {admin_addresses_filter}
            )
            select t.hash as id, '{context.project.name}' as project, m.source as user_address, t.now as ts 
            from transactions t
            join j_masters jm on t.account = jm.jetton_master_address
            join messages m on m.tx_hash = t.hash and m.direction = 'in'
            where compute_exit_code = 0 and action_result_code = 0
            and t.now >= {context.season.start_time}::integer
            and t.now < {context.season.end_time}::integer
            and {op_codes_filter}
        )
        """

"""
Jetton master interaction
Options:
* admin_addresses - list of admin addresses for jetton master
* op_codes - list of op codes (please use signed decimal notation, not hex!)
"""
class JettonMasterInteraction(Metric):
    def __init__(self, description, admin_addresses=[], op_codes=[]):
        Metric.__init__(self, description, [JettonMasterInteractionRedoubtImpl(), JettonMasterInteractionToncenterCppImpl()])
        assert type(admin_addresses) == list
        assert type(op_codes) == list
        self.admin_addresses = admin_addresses
        self.op_codes = op_codes
