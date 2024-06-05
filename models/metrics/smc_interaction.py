from models.metric import Metric, CalculationContext, TonalyticaMetricImpl


class SmartContractInteractionTonalyticaImpl(TonalyticaMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        return f"""
        select 
                msg_id as id, '{context.project.name}' as project, {0.5 if metric.is_custodial else 1} as weight, 
                source as user_address from messages_local m
        where destination ='{metric.address}' {'and length("comment") > 1' if metric.comment_required else ''}
        """


"""
Simple smart contract interaction - any message (but resulted in successful transaction) to the address provided
"""
class SmartContractInteraction(Metric):
    def __init__(self, description, address, is_custodial=False, comment_required=False):
        Metric.__init__(self, description, [SmartContractInteractionTonalyticaImpl()])
        self.address = address
        self.is_custodial = is_custodial
        self.comment_required = comment_required

