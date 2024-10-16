from typing import Dict

from models.backend import CalculationBackend
from models.backends import BACKEND_TONCENTER_CPP
from models.metric import MetricImpl, CalculationContext
from models.results import ProjectStat, CalculationResults
from models.season_config import SeasonConfig
import psycopg2
import psycopg2.extras
from loguru import logger
from backends.toncenter_cpp.utils import to_raw, to_user_friendly

class ToncenterCppNFTsBackend(CalculationBackend):
    def __init__(self, connection):
        CalculationBackend.__init__(self, "Toncenter CPP backend for NFTs leaderboard",
                                    leaderboards=[SeasonConfig.NFTS])
        self.connection = connection

    """
    Last block from the blockchain
    """
    def get_update_time(self, config: SeasonConfig):
        with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute("""
            select gen_utime as last_time from blocks
            where workchain = -1 and shard = -9223372036854775808 order by seqno desc limit 1
            """)
            return cursor.fetchone()['last_time']

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        logger.info("Running Toncenter CPP backend for NFTs leaderboard SQL generation")
        
        
        projects = []
        for project in config.projects:
            projects.append(f"select '{project.name}' as name, '{to_raw(project.address)}' as address, '{project.url if project.url else ''}' as url")
        PROJECTS = "\nunion all\n".join(projects)

        SQL = f"""
        with
        collections as (
            {PROJECTS}
        ),
        history as (
            select nh.*
            from parsed.nft_history nh 
            join collections c on c.address = nh.collection_address
            where event_type = 'sale'
            and utime > {config.start_time}::int
            and utime < {config.end_time}::int
        ),
        deals as (
            select nh.collection_address, nh.current_owner, nh.new_owner, nh.price, nh.marketplace
            from history nh 
            left join parsed.nft_history nh2 on nh.nft_item_address = nh2.nft_item_address and nh.current_owner = nh2.new_owner and nh.new_owner = nh2.current_owner
            where nh2.nft_item_address is null
            and nh.marketplace != '{to_raw("EQD_e1RdLx-t4-D0OCpxzsNFTDRBBpMkMi4TBQEz48awW_qW")}'
            and nh.marketplace != '{to_raw("EQC7rCsyYf4DVva0xOFfAOZbA2-g29FAQe4nhUqWAs1tC9hh")}'
        ),
        top as (
            select d.collection_address address, sum(d.price) / 1e9 volume
            from deals d
            group by d.collection_address
            order by volume desc
        )
        select address, name, url, coalesce(volume, 0) as volume from collections
        left join top using(address)
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
                    results[row['name']] = ProjectStat(
                        name=row['name'],
                        metrics={
                            ProjectStat.NFT_VOLUME: int(row['volume']),
                            ProjectStat.URL:  row['url'] if len(row['url']) > 0 else ("https://getgems.io/collection/" + to_user_friendly(row['address']))
                        }
                    )

            logger.info("NFT query finished")
        return CalculationResults(ranking=results.values(), build_time=1)

