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


class TokenTransferToJettonMasterRedoubtImpl(RedoubtMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        if len(metric.admin_addresses) > 0:
            admin_addresses_filter = " OR ".join(
                map(lambda addr: f"jm.admin_address = '{addr}'", metric.admin_addresses)
            )
        else:
            admin_addresses_filter = "FALSE"

        return f"""
        (
            with jetton_masters as (
                select jm.address as jetton_master_address from jetton_master jm
                where {admin_addresses_filter}
            )
            select jt.msg_id as id, '{context.project.name}' as project, 1 as weight,
            jt.source_owner as user_address
            from jetton_transfers_local jt
            join jetton_masters jm on jt.destination_owner = jm.jetton_master_address
            join jetton_masters jm2 on jt.jetton_master = jm2.jetton_master_address
            )
        )
        """


"""
Token (jetton) transfer from user to jetton masters related to specific list of admin addresses 
"""
class TokenTransferToJettonMaster(Metric):
    def __init__(self, description, admin_addresses=[]):
        Metric.__init__(self, description, [TokenTransferToJettonMasterRedoubtImpl()])
        assert type(admin_addresses) == list
        self.admin_addresses = admin_addresses


class ProxyContractInteractionRedoubtImpl(RedoubtMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        if len(metric.op_codes) > 0:
            op_codes_filter = " OR ".join(map(lambda op: f"m.op = {op}", metric.op_codes))
        else:
            op_codes_filter = "TRUE"
        return f"""
        (
            with proxy_contracts as (
                select distinct(address) from account_state where code_hash = {metric.code_hash}
            )
            select msg_id as id, '{context.project.name}' as project, 1 as weight, source as user_address 
            from messages_local m
            join proxy_contracts pc on pc.address = m.destination
            AND (
                {op_codes_filter}
            )
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
        Metric.__init__(self, description, [ProxyContractInteractionRedoubtImpl()])
        self.code_hash = code_hash
        self.op_codes = op_codes
