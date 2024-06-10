from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class ShardifyUnwrapRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        return f"""
        select  msg_id as id ,'Shardify' as project, 1 as weight, m.source as user_address 
        from messages_local m
        where destination in (select distinct address from account_state as2 where code_hash = '{metric.code_hash}')
        and op = 1150810207 and value = 2000000000
        """


"""
Specific metric for wNOT unwrap
code_hash - wNOT wallet code_hash
"""
class ShardifyUnwrap(Metric):
    def __init__(self, description, code_hash):
        Metric.__init__(self, description, [ShardifyUnwrapRedoubtImpl()])
        self.code_hash = code_hash

