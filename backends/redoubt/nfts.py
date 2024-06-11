from typing import Dict

from models.backend import CalculationBackend
from models.backends import BACKEND_REDOUBT
from models.metric import MetricImpl, CalculationContext
from models.results import ProjectStat, CalculationResults
from models.season_config import SeasonConfig
import psycopg2
import psycopg2.extras
from loguru import logger

class RedoubtNFTsBackend(CalculationBackend):
    def __init__(self, connection):
        CalculationBackend.__init__(self, "re:doubt backend for NFTs leaderboard",
                                    leaderboards=[SeasonConfig.NFTS])
        self.connection = connection

    """
    Update time for auxiliary table with messages
    """
    def get_update_time(self, config: SeasonConfig):
        with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute("""
            select bh.gen_utime as last_time
            from block_headers bh 
            join blocks b using(block_id)
            where b.masterchain_block_id is null 
            order by bh.gen_utime desc limit 1
            """)
            return cursor.fetchone()['last_time']

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        logger.info("Running re:doubt backend for NFTs leaderboard SQL generation")
        
        context = CalculationContext(season=config, impl=BACKEND_REDOUBT)
        
        projects = []
        for project in config.projects:
            projects.append(f"select '{project.name}' as name, '{project.address}' as address")
        PROJECTS = "\nunion all\n".join(projects)

        SQL = f"""
        with
        collections as (
            {PROJECTS}
        ),
        deals as (
            select nh.collection_address, nh.current_owner, nh.new_owner, nh.price, nh.marketplace
            from nft_history nh 
            join collections c on c.address = nh.collection_address
            where event_type = 'sale'
            and utime > {config.start_time}
            and utime < {config.end_time}
        ),
        top as (
            select d.collection_address address, sum(d.price) / 1e9 volume
            from deals d
            group by d.collection_address
            order by volume desc
        ),
        marketplaces as (
            select t.address, count(distinct d.marketplace) unique_marketplace_count
            from top t
            join deals d on t.address = d.collection_address
            group by address
        ),
        traders as (
            select d.collection_address, count(distinct trader) total_traders
            from top tp
            join deals d on tp.address = d.collection_address
            cross join unnest(array[d.current_owner, d.new_owner]) as t(trader)
            group by d.collection_address
        ),
        init_sales as (
            select nh.collection_address,
                nh.nft_item_address,
                nh.created_lt,
                nh.event_type,
                nh.price / 1e9 price
            from top t
            join nft_history nh on t.address = nh.collection_address 
            where nh.event_type in ('init_sale', 'cancel_sale', 'sale')
            and not nh.is_auction
            and nh.utime < {config.start_time}
        ),
        snapshot_price as (
            select distinct on (nft_item_address) *
            from init_sales
            order by nft_item_address, created_lt desc
        ),
        snapshot_floor_price as (
            select collection_address, min(price) snapshot_floor_price
            from snapshot_price
            where price > 0 and event_type = 'init_sale'
            group by collection_address
        ),
        snapshot_transfers as (
            select nh.collection_address,
                nh.nft_item_address,
                nh.created_lt,
                nh.new_owner 
            from top t
            left join nft_history nh on t.address = nh.collection_address 
            where nh.event_type in ('sale', 'transfer')
            and nh.utime < {config.start_time}
        ),
        snapshot_last_owners as (
            select distinct on (nft_item_address) collection_address, nft_item_address, new_owner "owner"
            from snapshot_transfers
            order by nft_item_address, created_lt desc
        ),
        full_snapshot_owners as (
            select mna.collection collection_address,
                case 
                    when slo."owner" is not null then slo."owner" else mna."owner" 
                end
            from mview_nft_actual mna
            left join snapshot_last_owners slo on slo.nft_item_address = mna.address  
        ),
        snapshot_holders as (
            select collection_address, count(distinct "owner") snapshot_holders
            from full_snapshot_owners
            group by collection_address
        ),
        current_stat as (
            select t.address, 
                nc."name", 
                t.volume, 
                count(1) total_items, 
                m.unique_marketplace_count,
                tr.total_traders,
                min(mna.price) filter (where mna.price > 0) / 1e9 floor_price,
                count(distinct mna."owner") holders
            from top t
            left join collections nc using(address)
            left join nft_item ni on ni.collection = nc.address 
            left join mview_nft_actual mna on mna.address = ni.address 
            left join traders tr on tr.collection_address = t.address
            join marketplaces m on m.address = t.address
            group by t.address, nc."name", t.volume, tr.total_traders, m.unique_marketplace_count
        )
        select cs.*, 
            sfp.snapshot_floor_price, 
            case 
                when sfp.snapshot_floor_price is not null then sh.snapshot_holders else null
            end snapshot_hoders
        from current_stat cs
        left join snapshot_floor_price sfp on cs.address = sfp.collection_address
        left join snapshot_holders sh on cs.address = sh.collection_address
        """
        logger.info(f"Generated SQL: {SQL}")

        results: Dict[str, ProjectStat] = {}

        if dry_run:
            logger.info("Running SQL query in dry_run mode")
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(f"explain {SQL}")
        else:
            logger.info("Running SQL query in production mode")
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(SQL)
                for row in cursor.fetchall():
                    logger.info(row)
                    assert row['project'] not in results
                    results[row['project']] = ProjectStat(
                        name=row['project'],
                        metrics={}
                    )
                    # TODO
                    # results[row['project']].metrics[ProjectStat.NFT_???] = int(row['???'])
            logger.info("NFT query finished")
        return CalculationResults(ranking=results.values(), build_time=1)

