from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


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
            jt.source_owner as user_address, ts
            from jetton_transfers_local jt
            join jetton_masters jm on jt.destination_owner = jm.jetton_master_address
            join jetton_masters jm2 on jt.jetton_master = jm2.jetton_master_address
        )
        """

class TokenTransferToJettonMasterToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        assert len(metric.admin_addresses) > 0
        admin_addresses_filter = " OR ".join(
                map(lambda addr: f"jm.admin_address = '{self.to_raw(addr)}'", metric.admin_addresses)
            )
        return f"""
(
            with target as (
                select jm.address as jetton_master_address from jetton_masters jm
                where {admin_addresses_filter}
            )
            select jt.tx_hash as id, '{context.project.name}' as project,
            jt.source as user_address, ts
            from jetton_transfers_local jt
            join target jm on jt.destination = jm.jetton_master_address and 
            jt.jetton_master_address = jm.jetton_master_address
        )
        """


"""
Token (jetton) transfer from user to jetton masters related to specific list of admin addresses 
"""
class TokenTransferToJettonMaster(Metric):
    def __init__(self, description, admin_addresses=[]):
        Metric.__init__(self, description, [TokenTransferToJettonMasterRedoubtImpl(), TokenTransferToJettonMasterToncenterCppImpl()])
        assert type(admin_addresses) == list
        self.admin_addresses = admin_addresses
