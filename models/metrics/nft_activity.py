from models.metric import Metric, CalculationContext, TonalyticaMetricImpl


class NFTActivityTonalyticaImpl(TonalyticaMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        collections = "\nor\n".join(map(lambda addr: f"collection  = '{addr}'", metric.collections))

        return f"""
        select id, '{context.project.name}' as project,
        {0.5 if metric.is_custodial else 1} as weight, 
        nft.user_address
        from nft_activity_local nft
        WHERE (
            {collections}
        )
        """


"""
All actions with NFTs for specified collections. Includes transfers and sales (activity by seller)
"""
class NFTActivity(Metric):
    def __init__(self, description, collections=[], is_custodial=False):
        Metric.__init__(self, description, [NFTActivityTonalyticaImpl()])
        self.collections = collections
        self.is_custodial = is_custodial

