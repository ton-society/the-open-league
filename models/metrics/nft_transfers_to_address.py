from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class NFTTransfersToAddressRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        return f"""
        select nt.msg_id as id, '{context.project.name}' as project, 1 as weight,
        current_owner as user_address, ts
        from nft_transfers_local nt
        where nt.new_owner = '{metric.address}'
        """


"""
All NFT transfers to the contract. 
"""
class NFTTransfersToAddress(Metric):
    def __init__(self, description, address):
        Metric.__init__(self, description, [NFTTransfersToAddressRedoubtImpl()])
        self.address = address

