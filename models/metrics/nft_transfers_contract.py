from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class NFTTransfersContractTypeRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):
        return f"""
        select nt.msg_id as id, '{context.project.name}' as project, 1 as weight,
        current_owner as user_address
        from nft_transfers_local nt
        where nt.new_owner in (select  distinct address from account_state as2 
          where as2.code_hash ='{metric.contract_code_hash}') 
          
        union all
        
        select nt.msg_id as id, '{context.project.name}' as project, 1 as weight,
        new_owner as user_address
        from nft_transfers_local nt
        where nt.current_owner in (select  distinct address from account_state as2 
          where as2.code_hash ='{metric.contract_code_hash}')
        
        """


"""
All actions with NFTs for specific sale contract.
Includes transfer to the contract (put on sale) and from (sales)
"""
class NFTTransfersContractType(Metric):
    def __init__(self, description, contract_code_hash):
        Metric.__init__(self, description, [NFTTransfersContractTypeRedoubtImpl()])
        self.contract_code_hash = contract_code_hash

