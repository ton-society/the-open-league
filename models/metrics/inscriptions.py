from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class InscriptionsRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        
        return f"""
        select 
                msg_id as id, '{context.project.name}' as project, 1 as weight, 
                source as user_address from messages_local m
        where comment like '%{metric.project_market}%'
        """


"""
Special filter for all messages using specific pattern in comment
"""
class Inscriptions(Metric):
    def __init__(self, description, project_market):
        Metric.__init__(self, description, [InscriptionsRedoubtImpl()])
        self.project_market = project_market
        
