from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class GasPumpJettonsBuysRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        """
        Calculation plan:
        1. Find all jetton masters that are owned by the admin addresses
        2. Find all messages that are sent to the jetton masters with the BUY_OP_CODE
        """

        BUY_OP_CODE = 1825825968
        admin_addresses_filter = " OR ".join(map(lambda addr: f"jm.admin_address = '{addr}'", metric.admin_addresses))

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
        where m.op = {BUY_OP_CODE}
        )
        """
    
class GasPumpJettonsBuysToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        BUY_OP_CODE = 1825825968
        admin_addresses_filter = " OR ".join(map(lambda addr: f"jm.admin_address = '{self.to_raw(addr)}'", metric.admin_addresses))

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
        and m.opcode = {BUY_OP_CODE}
        )
        """

"""
Counts all buys across all GasPump jettons
"""
class GasPumpJettonsBuys(Metric):
    def __init__(self, description, admin_addresses):
        Metric.__init__(self, description, [GasPumpJettonsBuysRedoubtImpl(), GasPumpJettonsBuysToncenterCppImpl()])
        assert type(admin_addresses) == list
        self.admin_addresses = admin_addresses


class GasPumpJettonsSellsAndUnwrapsRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        """
        Calculation plan:
        1. Find all jetton masters that are owned by the admin addresses
        2. Find all jetton burn messages for the jetton masters (sell and unwrap events are implemented as jetton burns in GasPump)
        """

        admin_addresses_filter = " OR ".join(map(lambda addr: f"jm.admin_address = '{addr}'", metric.admin_addresses))

        return f"""
        (
        with jetton_masters as (
            select jm.address as jetton_master_address from jetton_master jm
            where {admin_addresses_filter}
        )
        select
            jb.msg_id as id,
            '{context.project.name}' as project,
            1 as weight,
            jb.user_address as user_address, ts
        from jetton_burn_local jb
        join jetton_masters jm on jb.jetton_master = jm.jetton_master_address
        )
        """

class GasPumpJettonsSellsAndUnwrapsToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        admin_addresses_filter = " OR ".join(
            map(lambda addr: f"jm.admin_address = '{self.to_raw(addr)}'", metric.admin_addresses)
        )

        return f"""
        (
        with j_masters as (
            select jm.address as jetton_master_address from jetton_masters jm
            where {admin_addresses_filter}
        )
        select
            jb.tx_hash as id,
            '{context.project.name}' as project,
            jb.user_address as user_address, ts
        from jetton_burn_local jb
        join j_masters jm on jb.jetton_master_address = jm.jetton_master_address
        )
        """

"""
Counts all sells and unwraps across all GasPump jettons
"""
class GasPumpJettonsSellsAndUnwraps(Metric):
    def __init__(self, description, admin_addresses):
        Metric.__init__(self, description, [GasPumpJettonsSellsAndUnwrapsRedoubtImpl(), GasPumpJettonsSellsAndUnwrapsToncenterCppImpl()])
        assert type(admin_addresses) == list
        self.admin_addresses = admin_addresses