from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class InscriptionsRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        
        return f"""
        select 
                msg_id as id, '{context.project.name}' as project, 1 as weight, 
                source as user_address, ts from messages_local m
        where comment like '%{metric.project_market}%'
        """

class InscriptionsToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):
        return f"""
select '1' as id, 'x' as project, null as address, 1 as ts
        """

"""
Special filter for all messages using specific pattern in comment
"""
class Inscriptions(Metric):
    def __init__(self, description, project_market):
        Metric.__init__(self, description, [InscriptionsRedoubtImpl(), InscriptionsToncenterCppImpl()])
        self.project_market = project_market
        
