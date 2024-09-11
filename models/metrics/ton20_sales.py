from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class Ton20SalesRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):

        return f"""
        select id, '{context.project.name}' as project, 1 as weight, 
        buyer as user_address, ts
        from ton20_sale_local ts where
        ts.referral_address = '{metric.marketplace}'
        """


"""
Ton-20 smart-contract based sales
"""
class Ton20Sales(Metric):
    def __init__(self, description, marketplace):
        Metric.__init__(self, description, [Ton20SalesRedoubtImpl()])
        self.marketplace = marketplace

