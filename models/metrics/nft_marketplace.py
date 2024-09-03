from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class NFTMarketplaceRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):

        return f"""
        select id, '{context.project.name}' as project, 1 as weight, user_address, ts
        from nft_sales where marketplace = '{metric.marketplace}'
        """


"""
All sales-related operations for particular marketplace. Includes sales and init/cancel sale events
"""
class NFTMarketplace(Metric):
    def __init__(self, description, marketplace=""):
        Metric.__init__(self, description, [NFTMarketplaceRedoubtImpl()])
        self.marketplace = marketplace

