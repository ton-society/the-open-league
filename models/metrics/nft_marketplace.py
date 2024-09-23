from models.metric import Metric, CalculationContext, RedoubtMetricImpl, ToncenterCppMetricImpl


class NFTMarketplaceRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):

        return f"""
        select id, '{context.project.name}' as project, 1 as weight, user_address, ts
        from nft_sales where marketplace = '{metric.marketplace}'
        """

class NFTMarketplaceToncenterCppImpl(ToncenterCppMetricImpl):
    def calculate(self, context: CalculationContext, metric):

        return f"""
        select id, '{context.project.name}' as project, user_address, ts
        from nft_sales where marketplace = '{self.to_raw(metric.marketplace)}'
        """

"""
All sales-related operations for particular marketplace. Includes sales and init/cancel sale events
"""
class NFTMarketplace(Metric):
    def __init__(self, description, marketplace=""):
        Metric.__init__(self, description, [NFTMarketplaceRedoubtImpl(), NFTMarketplaceToncenterCppImpl()])
        self.marketplace = marketplace

