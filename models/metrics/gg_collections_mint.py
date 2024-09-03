from models.metric import Metric, CalculationContext, RedoubtMetricImpl


class GetGemsCollectionsMintsRedoubtImpl(RedoubtMetricImpl):

    def calculate(self, context: CalculationContext, metric):

        return f"""
        select id, '{context.project.name}' as project, 1 as weight, 
        (select destination from messages m where m.hash = nh.hash limit 1) as user_address, ts
        from nft_history_local nh where
        collection_address in (
            select distinct nc.address as collection  from nft_collection nc 
              where nc.metadata_url  like '%s.getgems.io%'
            except
            select address from tol.gg_banned_collections
        ) and event_type = 'mint'        
        """


"""
GetGems specific metrics, counts all mints for collections with off-chain metadata url
related to getgems.io
redoubt implementation also contains specific scam-related collections
in tol.gg_banned_collections table
"""
class GetGemsCollectionsMints(Metric):
    def __init__(self, description):
        Metric.__init__(self, description, [GetGemsCollectionsMintsRedoubtImpl()])

