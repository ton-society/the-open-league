import time
from typing import Dict

from models.backend import CalculationBackend
from models.backends import BACKEND_REDOUBT
from models.metric import MetricImpl, CalculationContext
from models.results import ProjectStat, CalculationResults
from models.scores import ScoreModel
from models.season_config import SeasonConfig
import psycopg2
import psycopg2.extras
from loguru import logger

class RedoubtAppBackend(CalculationBackend):
    def __init__(self, connection, mau_stats=False):
        CalculationBackend.__init__(self, "re:doubt backend for App leaderboard",
                                    leaderboards=[SeasonConfig.APPS])
        self.mau_stats = mau_stats
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
                    select '{project.name}' as symbol, '{project.token.address}' as address, 
                    {project.token.decimals} as decimals
                    """)
        PROJECTS = "\nunion all\n".join(PROJECTS)

        balances_table = "mview_jetton_balances"
        if (time.time()) > config.end_time:
            balances_table = f"tol.token_balances_snapshot_{config.safe_season_name()}"

        NEW_HOLDERS_SQL = f"""
            with tol_tokens as (
                {PROJECTS}                
            ),
            latest_balances as (
                select * from {balances_table}
            ), target_wallets as (
              -- target jetton wallets
              select distinct tol_tokens.symbol, tol_tokens.address, jw.address as wallet_address, jw.owner as owner_address from jetton_wallets jw
              join tol_tokens on jw.jetton_master = tol_tokens.address where not jw.is_scam
            ), wallet_activity as (
              -- all transfers by target wallets
              select symbol, tw.address, destination_owner as owner_address, utime as event_time
              from jetton_transfers jt
              join target_wallets tw on tw.wallet_address = jt.source_wallet and jt.successful
            ), first_activity as (
              -- timestamp of the first event
              select symbol, address, owner_address, min(event_time) as first_interaction
              from wallet_activity group by 1, 2, 3
            )  
            , new_holders as (
              -- new holder has a first incoming transfer during the season
              -- and currenly has 1+TON worth value of ton
              select  fa.symbol, count(distinct owner_address) as new_holders
              from first_activity fa
              join jetton_wallets jw on jw.jetton_master = fa.address and jw.owner = fa.owner_address
              join latest_balances mjb on mjb.wallet_address = jw.address
              where first_interaction >= {config.start_time} and first_interaction <  {config.end_time} and 
              mjb.balance / pow(10, (select decimals from tol_tokens tt where tt.symbol = fa.symbol))
              * (select price_ton from chartingview.token_agg_price_history taph where taph.address = fa.address
              and taph.build_time < to_timestamp({config.end_time} ) order by build_time desc limit 1)
              >= {config.score_model.param(ScoreModel.PARAM_TOKEN_MIN_VALUE_FOR_NEW_HOLDER)}
              -- new holder should have deployed wallet. at least at the past.
              and exists (select from account_state as2 where as2.address = owner_address and code_hash is not null)
              and not exists (select from tol.banned_users b where b.address = owner_address)
              group by 1
            )
            select tol_tokens.symbol,
            tol_tokens.address,
            coalesce(new_holders, 0) as new_holders
            from tol_tokens
            left join new_holders on new_holders.symbol = tol_tokens.symbol
        """
        logger.info(f"Generated SQL: {NEW_HOLDERS_SQL}")

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
        if self.mau_stats:
            messages = f"""
            -- full messages table, filter by last 30 days
            select m.*
            from  transactions t
            join messages m on m.in_tx_id  = t.tx_id
    
            where
            t.utime >= {config.start_time}::int and t.utime < {config.end_time}::int
            and (
                        (t.action_result_code  = 0 and t.compute_exit_code  = 0)
                        or
                        (t.action_result_code is null and t.compute_exit_code  is null and t.compute_skip_reason = 'cskip_no_gas')
            )
            """
            final_part = f"""
            insert into tol.daily_app_users(project, user_address, tx_count, period_start, period_end)
            select project, user_address, tx_count, {config.start_time}::int as period_start, {config.end_time}::int as period_end from users_stats
            """
        else:
            messages = f"""
            -- we will use subset of messages table for better performance
            -- also this table contains only messages with successful destination tx
            select * from tol.messages_{config.safe_season_name()}
            """
            final_part = """
            , good_users as (
            select
              project,
              sum(weight) filter (where tx_count > 1) as total_users, -- users with 2+ tx, custodial wallets have lower weight
              percentile_disc(0.5) within group (order by tx_count) as median_tx  -- median tx per user 
            from users_stats
            group by 1
            ), tx_stat as (
            select project, sum(weight * tx_count) as tx_count from users_stats
            group by 1
            )
            select project, coalesce(tx_count, 0) as tx_count,  coalesce(total_users,0 )as total_users, 
            coalesce(median_tx, 0) as median_tx, url, prizes, possible_reward
            from project_names
            left join tx_stat using(project)
                     left join good_users using(project)
            """
        SQL = f"""
        with messages_local as (
            {messages}            
        ), jetton_transfers_local as (
            select jt.*, jw.jetton_master from jetton_transfers jt
            JOIN jetton_wallets jw ON jw.address = jt.source_wallet and not jw.is_scam
            where
                jt.successful and
                jt.utime >= {config.start_time}::int and
                jt.utime <  {config.end_time}::int
        ), nft_activity_local as (
          select msg_id as id, nt.current_owner as user_address, ni.collection  from nft_transfers nt
                                                                               join nft_item ni on nt.nft_item = ni.address
            where nt.utime >= {config.start_time}::int  and nt.utime <  {config.end_time}::int
              and collection is not null
            union
            select msg_id as id, new_owner as user_address, collection_address as collection
            from nft_history nh where event_type ='sale'
                                  and utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), nft_history_local as (
            select  * from nft_history
            where utime  >= {config.start_time}::int and utime  < {config.end_time}::int
        ), nft_transfers_local as (
            select  * from nft_transfers
            where utime  >= {config.start_time}::int and utime  < {config.end_time}::int
        ), ton20_sale_local as (
            select * from ton20_sale ts
            where utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), jetton_burn_local as (
            select jb.*, jw."owner" as user_address, jw.jetton_master from jetton_burn jb
            join jetton_wallets jw on jw.address  = jb.wallet and jb.successful and not jw.is_scam
            where utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), jetton_mint_local as (
            select jm.*, jw."owner" as user_address, jw.jetton_master from jetton_mint jm
            join jetton_wallets jw on jw.address  = jm.wallet and jm.successful and not jw.is_scam
            where utime >= {config.start_time}::int  and utime <  {config.end_time}::int
        ), dex_swaps_local as (
            select * from dex_swap_parsed
            where swap_utime >= {config.start_time}::int  and swap_utime <  {config.end_time}::int
        ),      
        nft_sales as (
            select msg_id as id, nh.current_owner  as user_address, marketplace from nft_history_local nh where
            (event_type = 'init_sale' or event_type = 'cancel_sale')
            
            union all
            
            select msg_id as id, nh.new_owner as user_address, marketplace from nft_history_local nh where
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
        )
        , users_stats_raw as (
          select project, user_address, min(weight) as weight, count(distinct id) as tx_count from all_projects
          group by 1, 2
        ), users as (
         select distinct user_address from users_stats_raw
        ),
        states as (
          -- get code hash 
         select distinct on (as2.address)  usr.user_address, code_hash from account_state as2
         join users usr on usr.user_address = as2.address
         order by address, last_tx_lt desc
        ), wallets as (
         select user_address from states where
         code_hash is null or
           code_hash = '/rX/aCDi/w2Ug+fg1iyBfYRniftK5YDIeIZtlZ2r1cA='   or   -- wallet v4 r2
           code_hash = 'hNr6RJ+Ypph3ibojI1gHK8D3bcRSQAKl0JGLmnXS1Zk='   or   -- wallet v3 r2
           code_hash = 'thBBpYp5gLlG6PueGY48kE0keZ/6NldOpCUcQaVm9YE='   or   -- wallet v3 r1
           code_hash = 'ZN1UgFUixb6KnbWc6gEFzPDQh4bKeb64y3nogKjXMi0='   or   -- wallet v4 r1
           code_hash = 'MZrVLsmoWWIPil2Ww2CJ5nw29OOTAdBQ224VCXAZzpE='   or   -- wallet_v5_beta
           code_hash = 'WHzHie/xyE9G7DeX5F/ICaFP9a4k8eDHpqmcydyQYf8='   or   -- wallet v1 r3
           code_hash = 'XJpeaMEI4YchoHxC+ZVr+zmtd+xtYktgxXbsiO7mUyk='   or   -- wallet v2 r1
           code_hash = '/pUw0yQ4Uwg+8u8LTCkIwKv2+hwx6iQ6rKpb+MfXU/E='   or   -- wallet v2 r2
           code_hash = 'oM/CxIruFqJx8s/AtzgtgXVs7LEBfQd/qqs7tgL2how='   or   -- wallet v1 r1
           code_hash = '1JAvzJ+tdGmPqONTIgpo2g3PcuMryy657gQhfBfTBiw='        -- wallet v1 r2
        ),
        users_stats as (
          select * from users_stats_raw
          join wallets using(user_address)
        )
        {final_part}
        """
        logger.info(f"Generated SQL: {SQL}")

        results: Dict[str, ProjectStat] = {}

        if self.mau_stats:
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                logger.info("Executing insert")
                cursor.execute(SQL)
                logger.info("Query finished")
                return
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
                    results[row['project']].metrics[ProjectStat.URL] = row['url']
                    results[row['project']].metrics[ProjectStat.PRIZES] = row['prizes']
                    results[row['project']].metrics[ProjectStat.REWARD] = 0
                    results[row['project']].metrics[ProjectStat.POSSIBLE_REWARD] = row['possible_reward']
                    results[row['project']].metrics[ProjectStat.APP_ONCHAIN_TOTAL_TX] = int(row['tx_count'])
                    results[row['project']].metrics[ProjectStat.APP_ONCHAIN_UAW] = int(row['total_users'])
                    results[row['project']].metrics[ProjectStat.APP_ONCHAIN_MEDIAN_TX] = int(row['median_tx'])
                    results[row['project']].metrics[ProjectStat.TOKEN_NEW_USERS_WITH_MIN_AMOUNT] = 0
            logger.info("Main query finished")
        if not dry_run:
            logger.info("Requesting off-chain tganalytics.xyz metrics")
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                for project in config.projects:
                    if project.analytics_key is None:
                        logger.info(f"Project {project.name} has no off-chain tracking activity")
                        if project.name in results:
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_NON_PREMIUM_USERS] = 0
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_PREMIUM_USERS] = 0
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_AVG_DAU] = 0
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_TOTAL_USERS] = 0
                            results[project.name].metrics[ProjectStat.APP_STICKINESS] = 0
                        continue

                    logger.info(f"Requesting data for {project.name} ({project.analytics_key}) ({config.name})")
                    cursor.execute("""
                    select * from tol.tganalytics_latest where app_name = %s and season = %s
                    """, (project.analytics_key, config.name))
                    res = cursor.fetchone()
                    if not res:
                        logger.error(f"No off-chain data for {project.name}")
                        results[project.name].metrics[ProjectStat.APP_OFFCHAIN_NON_PREMIUM_USERS] = 0
                        results[project.name].metrics[ProjectStat.APP_OFFCHAIN_PREMIUM_USERS] = 0
                        results[project.name].metrics[ProjectStat.APP_OFFCHAIN_AVG_DAU] = 0
                        results[project.name].metrics[ProjectStat.APP_OFFCHAIN_TOTAL_USERS] = 0
                        results[project.name].metrics[ProjectStat.APP_STICKINESS] = 0
                    else:
                        if project.name not in results:
                            logger.error(f"Project {project.name} has no on-chain data, ignoring")
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_NON_PREMIUM_USERS] = 0
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_PREMIUM_USERS] = 0
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_AVG_DAU] = 0
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_TOTAL_USERS] = 0
                            results[project.name].metrics[ProjectStat.APP_STICKINESS] = 0
                        else:
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_NON_PREMIUM_USERS] = int(res['non_premium_users'])
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_PREMIUM_USERS] = int(res['premium_users'])
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_AVG_DAU] = int(res['avg_dau'])
                            results[project.name].metrics[ProjectStat.APP_OFFCHAIN_TOTAL_USERS] = int(res['total_unique_users'])
                            results[project.name].metrics[ProjectStat.APP_STICKINESS] = 100.0 * int(res['avg_dau']) / int(res['total_unique_users'])


            logger.info("Off-chain processing is finished")


            logger.info("Requesting token new holders")
            with self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute(NEW_HOLDERS_SQL)
                for row in cursor.fetchall():
                    results[row['symbol']].metrics[ProjectStat.TOKEN_NEW_USERS_WITH_MIN_AMOUNT] = int(row['new_holders'])
                    results[row['symbol']].metrics[ProjectStat.TOKEN_ADDRESS] = row['address']
            
        return CalculationResults(ranking=results.values(), build_time=1)  # TODO build time


    def _generate_project_block(self, config: SeasonConfig, metric: MetricImpl):
        return metric.calculate(config)
