from models.metric import Metric, CalculationContext, RedoubtMetricImpl


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
                m.source as user_address
            from messages_local m
            join jetton_masters jm on m.destination = jm.jetton_master_address
            where {op_codes_filter}
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
        Metric.__init__(self, description, [JettonMasterInteractionRedoubtImpl()])
        assert type(admin_addresses) == list
        assert type(op_codes) == list
        self.admin_addresses = admin_addresses
        self.op_codes = op_codes
