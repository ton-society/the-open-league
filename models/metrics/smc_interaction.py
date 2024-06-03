from models.metric import Metric, CalculationContext, TonalyticaMetricImpl


class SmartContractInteractionTonalyticaImpl(TonalyticaMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        return f"""
        select 
                msg_id as id, '{context.project.name}' as project, 
                source as user_address from messages_local m
        where destination ='{metric.address}'
        """


class SmartContractInteraction(Metric):
    def __init__(self, description, address):
        Metric.__init__(self, description, [SmartContractInteractionTonalyticaImpl()])
        self.address = address
        # TODO - more flags

