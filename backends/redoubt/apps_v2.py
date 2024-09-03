import time
from typing import Dict

from models.backend import CalculationBackend
from models.backends import BACKEND_REDOUBT
from models.metric import MetricImpl, CalculationContext
from models.results import ProjectStat, CalculationResults
from models.scores import ScoreModel
from models.season_config import SeasonConfig
import psycopg2
import json
import psycopg2.extras
from loguru import logger

"""
Second version of redoubt backed apps backend.
It aggregates all actions by the users on the daily basis and stores number of days with activity by the user.
Results are stored directly to the table with the following structure:
create table tol.apps_users_stats_{season_name}(
id serial primary key,
project varchar,
address varchar,
days smallint[],
added_at timestamp default now()
)
create unique index unique_apps_users_stats_{season_name} on tol.apps_users_stats_{season_name} (project, address)
"""

class RedoubtAppBackendV2(CalculationBackend):
    def __init__(self, connection):
        CalculationBackend.__init__(self, "re:doubt backend for App leaderboard",
                                    leaderboards=[SeasonConfig.APPS])
        self.connection = connection

    """
    Update time for auxiliary table with messages
    """
    def get_update_time(self, config: SeasonConfig):
        with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
            cursor.execute(f"""
            select coalesce( (select utime from transactions t where t.tx_id = m.in_tx_id),
            (select utime from transactions t where t.tx_id = m.out_tx_id)) as last_time
            from tol.messages_{config.safe_season_name()} m
            order by msg_id desc limit 1
            """)
            return cursor.fetchone()['last_time']

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        logger.info("Requesting token new holders stats for the apps with tokens")
        PROJECTS = []

        for project in config.projects:
            if project.token is not None:
                PROJECTS.append(f"""
                    select '{project.name}' as project, '{project.token.address}' as address, 
                    {project.token.decimals} as decimals, 
                    """)
        PROJECTS = "\nunion all\n".join(PROJECTS)

        balances_table = "mview_jetton_balances"
        if (time.time()) > config.end_time:
            balances_table = f"tol.token_balances_snapshot_{config.safe_season_name()}"


        logger.info("Running re:doubt backend for App leaderboard SQL generation")
        PROJECTS = []
        PROJECTS_ALIASES = []
        PROJECTS_NAMES = []
        context = CalculationContext(season=config, impl=BACKEND_REDOUBT)
        
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
            select '{project.name}' as project, {project.prizes} as prizes, {project.possible_reward} as possible_reward,
            '{project.url if project.url else ""}' as url
            """)
        PROJECTS = ",\n".join(PROJECTS)
        PROJECTS_ALIASES = "\nUNION ALL\n".join(PROJECTS_ALIASES)
        PROJECTS_NAMES = "\nUNION ALL\n".join(PROJECTS_NAMES)
        messages = f"""
        -- we will use subset of messages table for better performance
        -- also this table contains only messages with successful destination tx
        select * from tol.messages_{config.safe_season_name()}
        """

        SQL = f"""
        insert into tol.apps_users_stats_{config.safe_season_name()} (project, address, days)
        with messages_local as (
            {messages}            
        ), jetton_transfers_local as (
            select jt.*, jw.jetton_master, jt.utime as ts from jetton_transfers jt
            JOIN jetton_wallets jw ON jw.address = jt.source_wallet and not jw.is_scam
            where
                jt.successful and
                jt.utime >= {config.start_time}::int and
                jt.utime <  {config.end_time}::int
        ), nft_activity_local as (
          select msg_id as id, nt.current_owner as user_address, ni.collection, nt.utime as ts  from nft_transfers nt
                                                                               join nft_item ni on nt.nft_item = ni.address
            where nt.utime >= {config.start_time}::int  and nt.utime <  {config.end_time}::int
              and collection is not null
            union
            select msg_id as id, new_owner as user_address, collection_address as collection, utime as ts
            from nft_history nh where event_type ='sale'
                                  and utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), nft_history_local as (
            select  *, utime as ts from nft_history
            where utime  >= {config.start_time}::int and utime  < {config.end_time}::int
        ), nft_transfers_local as (
            select  *, utime as ts from nft_transfers
            where utime  >= {config.start_time}::int and utime  < {config.end_time}::int
        ), ton20_sale_local as (
            select *, utime as ts from ton20_sale ts
            where utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), jetton_burn_local as (
            select jb.*, jw."owner" as user_address, jw.jetton_master, jb.utime as ts from jetton_burn jb
            join jetton_wallets jw on jw.address  = jb.wallet and jb.successful and not jw.is_scam
            where utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), jetton_mint_local as (
            select jm.*, jw."owner" as user_address, jw.jetton_master, utime as ts from jetton_mint jm
            join jetton_wallets jw on jw.address  = jm.wallet and jm.successful and not jw.is_scam
            where utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), dex_swaps_local as (
            select *, swap_utime as ts from dex_swap_parsed
            where swap_utime >= {config.start_time}::int  and swap_utime <  {config.end_time}::int
        ),      
        nft_sales as (
            select msg_id as id, nh.current_owner  as user_address, marketplace, ts from nft_history_local nh where
            (event_type = 'init_sale' or event_type = 'cancel_sale')
            
            union all
            
            select msg_id as id, nh.new_owner as user_address, marketplace, ts from nft_history_local nh where
            event_type = 'sale'
        ),
        {PROJECTS},
        all_projects_raw as (
        {PROJECTS_ALIASES}        
        ), project_names as (
        {PROJECTS_NAMES}
        ),
        all_projects as (
          -- exclude banned users
         select f.* from all_projects_raw f
         left join tol.banned_users b on b.address = f.user_address -- exclude banned users
         where b.address is null
        ), events_with_days as (
            -- adding day since the start of the season
            select *, (ts - {config.start_time}::int) / 86400 + 1 as day from all_projects_raw
        )
        select project, user_address, array_agg(distinct day) as days from events_with_days
        group by 1, 2
        on conflict (project, address) do update SET days = EXCLUDED.days
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
            self.connection.commit()
            logger.info("Main query finished")
            
        return CalculationResults(ranking=results.values(), build_time=1)


    def _generate_project_block(self, config: SeasonConfig, metric: MetricImpl):
        return metric.calculate(config)
