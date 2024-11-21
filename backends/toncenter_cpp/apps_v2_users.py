import time
from typing import Dict
from backends.toncenter_cpp.utils import to_raw

from models.backend import CalculationBackend
from models.backends import BACKEND_REDOUBT, BACKEND_TONCENTER_CPP
from models.metric import MetricImpl, CalculationContext
from models.results import ProjectStat, CalculationResults
from models.scores import ScoreModel
from models.season_config import SeasonConfig
import psycopg2
import json
import psycopg2.extras
from loguru import logger

"""
Apps backend for S6. This implementation is based on toncenter-cpp indexer data mart.

It aggregates all actions by the users on the daily basis and stores number of days with activity by the user.
Results are stored directly to the table with the following structure:

create table tol.apps_users_stats_{season_name}(
id serial primary key,
project varchar,
address varchar,
days smallint[],
token_value_ton decimal(10, 2),
nfts_count int8,
added_at timestamp default now(),
updated_at timestamp,
unique (project, address)
)
"""

class ToncenterCppAppBackendV2Users(CalculationBackend):
    def __init__(self, connection, produce_output=False):
        CalculationBackend.__init__(self, "Toncenter CPP backend for App leaderboard",
                                    leaderboards=[SeasonConfig.APPS])
        self.connection = connection
        self.produce_output = produce_output

    """
    Update time for auxiliary table with messages
    """
    def get_update_time(self, config: SeasonConfig):
        with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute("""
            select gen_utime as last_time from blocks
            where workchain = -1 and shard = -9223372036854775808 order by seqno desc limit 1
            """)
            return cursor.fetchone()['last_time']

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        TOKENS = []
        PROJECT_NFTS = []

        for project in config.projects:
            if project.token is not None:
                TOKENS.append(f"""
                    select '{project.name}' as project, '{to_raw(project.token.address)}' as address, 
                    {project.token.decimals} as decimals
                    """)
            if project.nfts is not None:
                for nft in project.nfts:
                    PROJECT_NFTS.append(f"""
                        select '{project.name}' as project, '{to_raw(nft)}' as address
                        """)
        TOKENS = "\nunion all\n".join(TOKENS)
        PROJECT_NFTS = "\nunion all\n".join(PROJECT_NFTS)

        balances_table = "tol.jetton_wallets_S6_end_normie"        
        nft_table = "tol.nft_items_s6_end"


        logger.info("Running backend for App leaderboard SQL generation")
        PROJECTS = []
        PROJECTS_ALIASES = []
        PROJECTS_NAMES = []
        context = CalculationContext(season=config, impl=BACKEND_TONCENTER_CPP)
        
        for project in config.projects:
            context.project = project
            metrics = []
            for metric in project.metrics:
                metrics.append(metric.calculate(context))
            if len(metrics) > 0:
                metrics = "\nUNION ALL\n".join(metrics)
                PROJECTS.append(f"""
                project_{project.name_safe()} as (
                {metrics}
                )
                """)
                PROJECTS_ALIASES.append(f"""
                select * from project_{project.name_safe()}
                """)
            PROJECTS_NAMES.append(f"""
            select '{project.name}' as project
            """)
        PROJECTS = ",\n".join(PROJECTS)
        PROJECTS_ALIASES = "\nUNION ALL\n".join(PROJECTS_ALIASES)
        PROJECTS_NAMES = "\nUNION ALL\n".join(PROJECTS_NAMES)

        SQL = f"""
        with jetton_transfers_local as (
            select jt.*, jt.tx_now as ts from jetton_transfers jt
            where
                jt.tx_now >= {config.start_time}::int and
                jt.tx_now <  {config.end_time}::int and not tx_aborted
        ), nft_activity_local as (
          select tx_hash as id, current_owner as user_address, collection_address as collection, utime as ts
            from parsed.nft_history nh where event_type ='transfer'
                                  and utime >= {config.start_time}::int  and utime <  {config.end_time}::int
            union
            select tx_hash as id, new_owner as user_address, collection_address as collection, utime as ts
            from parsed.nft_history nh where event_type ='sale'
                                  and utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), nft_history_local as (
            select  tx_hash as id, *, utime as ts from parsed.nft_history
            where utime  >= {config.start_time}::int and utime  < {config.end_time}::int
        ), nft_transfers_local as (
            select  *, tx_now as ts from public.nft_transfers
            where tx_now  >= {config.start_time}::int and tx_now  < {config.end_time}::int and not tx_aborted
        ), jetton_burn_local as (
            select jb.*, "owner" as user_address, tx_now as ts from jetton_burns jb
            where tx_now >= {config.start_time}::int  and tx_now <  {config.end_time}::int
        ), jetton_mint_local as (
            select 1
        ), dex_swaps_local as (
            select *, swap_utime as ts from parsed.dex_swap_parsed
            where swap_utime >= {config.start_time}::int  and swap_utime <  {config.end_time}::int
        ),      
        nft_sales as (
            select tx_hash as id, nh.current_owner  as user_address, marketplace, ts from nft_history_local nh where
            (event_type = 'init_sale' or event_type = 'cancel_sale')
            
            union all
            
            select tx_hash as id, nh.new_owner as user_address, marketplace, ts from nft_history_local nh where
            event_type = 'sale'
        ),
        {PROJECTS},
        all_projects_raw as (
        {PROJECTS_ALIASES}        
        ), project_names as (
        {PROJECTS_NAMES}
        ), tokens as (
            {TOKENS}
        ), nfts as (
            {PROJECT_NFTS}
        ), tokens_price as (
           select project, tokens.address,
             (select price_ton / 1e9 from prices.agg_prices ap where ap.base = tokens.address
             and ap.price_time < {config.end_time}::int order by price_time desc limit 1) as price_ton
              from tokens
        ),all_projects as (
          -- TODO exclude banned users
         select f.* from all_projects_raw f
         -- left join tol.banned_users b on b.address = f.user_address -- exclude banned users
         --where b.address is null
        ), events_with_days as (
            -- adding day since the start of the season
            select *, (ts - {config.start_time}::int) / 86400 + 1 as day from all_projects
        ), results as (
        select project, user_address, array_agg(distinct day) as days from events_with_days
        group by 1, 2
        ), tokens_holders as (
            select r.project, r.user_address, tp.price_ton * b.balance as token_value_ton from results r
            join tokens_price tp on tp.project = r.project
            join {balances_table} b on b.jetton = tp.address and b."owner" = r.user_address
        ), nft_holders as (
            select r.project, r.user_address, count(1) as nfts_count from results r
            join nfts on nfts.project = r.project
            join {nft_table} n on n.collection_address = nfts.address and n.owner_address = r.user_address
            group by 1, 2
        ), output as (
          select results.*, coalesce(th.token_value_ton, 0) as token_value_ton, coalesce(nh.nfts_count, 0) as nfts_count, 
          now() as updated from results 
          left join tokens_holders th on results.project = th.project and results.user_address = th.user_address
          left join nft_holders nh on results.project = nh.project and results.user_address = nh.user_address
        )
        """

        if self.produce_output:
            SQL = f"""
{SQL}
select project, count(distinct user_address) as uaw from all_projects
        group by 1
            """
        else:
            SQL = f"""
insert into tol.apps_users_stats_{config.safe_season_name()} (project, address, days, token_value_ton, nfts_count, updated_at)
{SQL}
select * from output
on conflict (project, address) do update SET
    days = EXCLUDED.days,
    token_value_ton = EXCLUDED.token_value_ton,
    nfts_count = EXCLUDED.nfts_count
"""

        def add_lines(s):
            # return s
            out = []
            i = 1
            for line in s.split("\n"):
                out.append("%d: %s" % (i, line))
                i += 1
            return "\n".join(out)
        logger.info(f"Generated SQL: {add_lines(SQL)}")

        results: Dict[str, ProjectStat] = {}

        if dry_run:
            logger.info("Running SQL query in dry_run mode")
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(f"explain {SQL}")
        else:
            logger.info("Running SQL query in production mode")
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(SQL)
                if self.produce_output:
                    logger.info("Generating output values")
                    for row in cursor.fetchall():
                        results[row['project']] = ProjectStat(
                            name=row['project'],
                            metrics={
                                ProjectStat.APP_ONCHAIN_UAW: row['uaw'],
                                ProjectStat.APP_ONCHAIN_ENROLLED_UAW: 0,
                                ProjectStat.APP_AVERAGE_SCORE: 0,
                                ProjectStat.APP_TOTAL_POINTS: 0
                            }
                        )
                else:
                    self.connection.commit()
            logger.info("Main query finished")
            
        return CalculationResults(ranking=results.values(), build_time=1)


    def _generate_project_block(self, config: SeasonConfig, metric: MetricImpl):
        return metric.calculate(config)
