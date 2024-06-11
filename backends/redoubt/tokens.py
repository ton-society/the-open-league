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

class RedoubtTokensBackend(CalculationBackend):
    def __init__(self):
        CalculationBackend.__init__(self, "re:doubt backend for Tokens leaderboard",
                                    leaderboards=[SeasonConfig.TOKENS])

    def get_update_time(self, config: SeasonConfig):
        with psycopg2.connect() as pg:
            with pg.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                cursor.execute("""
                select extract('epoch' from update_time) as update_time  from chartingview.token_agg_price tap order by update_time desc limit 1
                """)
                return cursor.fetchone()['update_time']

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        logger.info("Running re:doubt backend for Token leaderboard SQL generation")
        PROJECTS = []
        # context = CalculationContext(season=config, impl=BACKEND_REDOUBT)
        for project in config.projects:
            PROJECTS.append(f"""
            select '{project.name}' as symbol, '{project.address}' as address, {project.decimals} as decimals,
            {project.is_meme} as is_meme, {project.has_boost} as has_boost
            """)
        PROJECTS = "\nunion all\n".join(PROJECTS)

        balances_table = "mview_jetton_balances"
        if (time.time()) > config.end_time:
            balances_table = f"tol.token_balances_snapshot_{config.safe_season_name()}"
        SQL = f"""
            with tol_tokens as (
                {PROJECTS}                
            ), tol_ton_or_stable as (
            -- allowed tokens for pairs - TON or stable or LSDs
                select 'EQBPAVa6fjMigxsnHF33UQ3auufVrg2Z8lBZTY9R-isfjIFr' as address union all
                select 'EQDQoc5M3Bh8eWFephi9bClhevelbZZvWhkqdo80XuY_0qXv' as address union all
                select 'EQCM3B12QK1e4yZSf8GtBRT0aLMNyEsBc_DhVfRRtOEffLez' as address union all
                select 'EQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM9c' as address union all
                select 'EQCajaUU1XXSAjTD-xOV7pE49fGtg4q8kF3ELCOJtGvQFQ2C' as address union all
                select 'EQB-MPwrd1G6WKNkLz_VnV6WqBDd142KMQv-g1O-8QUA3728' as address union all
                select 'EQBynBO23ywHy_CgarY9NK9FTz0yDsG82PtcbSTQgGoXwiuA' as address union all
                select 'EQC_1YoM8RBixN95lz7odcF3Vrkc_N8Ne7gQi7Abtlet_Efi' as address union all
                select 'EQC61IQRl0_la95t27xhIpjxZt32vl1QQVF2UgTNuvD18W-4' as address union all
                select 'EQCxE6mUtQJKFnGfaROTKOt1lZbDiiX1kCixRv7Nw2Id_sDs' as address union all
                select 'EQDNhy-nxYFgUqzfUzImBEP67JqsyMIcyk2S5_RwNNEYku0k' as address union all
                select 'EQC98_qAmNEptUtPc7W6xdHh_ZHrBUFpw5Ft_IzNU20QAJav' as address union all
                select 'EQDPdq8xjAhytYqfGSX8KcFWIReCufsB9Wdg0pLlYSO_h76w' as address 
            ),
            latest_balances as (
                select * from {balances_table}
            ), pools as (
              -- all DEX pools for our tokens
              select distinct tol_tokens.symbol, tol_tokens.address, thd.address as pool
              from tvl_history_datamart thd join tol_tokens on tol_tokens.address = thd.jetton_a
              where jetton_b in (select address from tol_ton_or_stable)
              and build_time >=  to_timestamp({config.start_time}) - interval '7 day'
              union
              select distinct tol_tokens.symbol, tol_tokens.address, thd.address as pool
              from tvl_history_datamart thd join tol_tokens on tol_tokens.address = thd.jetton_b
              where jetton_a in (select address from tol_ton_or_stable)
              and build_time >=  to_timestamp({config.start_time}) - interval '7 day'
            ), tvl_prior_start as (
              -- TVL for 7 days before the start
              select build_time, p.symbol, sum(tvl_ton) as tvl
              from tvl_history_datamart thd join pools p on thd.address = p.pool
              and build_time >=  to_timestamp({config.start_time}) - interval '7 day'
              and build_time <  to_timestamp({config.start_time})
              group by 1, 2
            ), avg_tvl_prior_start as (
              -- average it
              select symbol, count(1) as cnt, round(avg(tvl)) as start_tvl from tvl_prior_start
              group by 1
            ), current_tvl as (
              -- TVL during the season
              select build_time, p.symbol, sum(tvl_ton) as tvl
              from tvl_history_datamart thd join pools p on thd.address = p.pool
              and build_time >=  to_timestamp({config.start_time})
              and build_time <  to_timestamp({config.end_time})
              group by 1, 2
            ), last_tvl as (
              -- latest values
              select distinct on (symbol) symbol, tvl from current_tvl
              order by symbol, build_time desc
            ), avg_daily_tvl as (
              -- avg daily TVL
              select symbol, build_time::date as bd, avg(tvl) as tvl from current_tvl
              group by 1, 2
            ), days_with_tvl as (
              -- days with TVL (if project created during the season it would be less)
              select symbol, count(1) as days from avg_daily_tvl
              group by 1
            ), tvl_weighted as (
              -- calcylate weighted TVL change for each project
              select symbol, start_tvl, days, sum(tvl - start_tvl) / days as tvl_change from avg_daily_tvl
              join days_with_tvl using(symbol)
              join avg_tvl_prior_start using(symbol)
              group by 1, 2, 3
            ), target_wallets as (
              -- target jetton wallets
              select distinct tol_tokens.symbol, tol_tokens.address, jw.address as wallet_address, jw.owner as owner_address from jetton_wallets jw
              join tol_tokens on jw.jetton_master = tol_tokens.address where not jw.is_scam
            ), wallet_activity as (
              -- all transfers by target wallets
              -- TODO - add filter on the start/end date?
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
              group by 1
            )
            , price_snapshots as (
              -- price value before the start  and at the end
              select symbol, (
                select price_ton from chartingview.token_agg_price_history ph where ph.address = tt.address
                and build_time < to_timestamp({config.start_time} ) order by build_time desc limit 1
              ) as price_before, (
                select price_ton from chartingview.token_agg_price_history ph where ph.address = tt.address
                and build_time <= to_timestamp({config.end_time} ) order by build_time desc limit 1
              )  as price_after from tol_tokens tt
            ), price_delta as (
              select symbol, price_before, price_after, case
                when price_before is null then 0
                else (price_after - price_before) / (price_before)
              end as price_change
              from price_snapshots
            )
            select tvl_weighted.symbol,
            (select address from tol_tokens where tol_tokens.symbol = tvl_weighted.symbol limit 1) as address,
            (select is_meme from tol_tokens where tol_tokens.symbol = tvl_weighted.symbol limit 1) as is_meme,
            (select has_boost from tol_tokens where tol_tokens.symbol = tvl_weighted.symbol limit 1) as has_boost,
            tvl_change, start_tvl,
            coalesce(new_holders, 0) as new_holders,
            last_tvl.tvl as last_tvl,
            100 * coalesce(price_change, 0) as price_delta,
            100 * coalesce(price_change, 0) * ( sqrt(last_tvl.tvl) / 1000) as price_delta_normed,
            coalesce(price_before, 0) as price_before,
            coalesce(price_after, 0) as price_after
            from tvl_weighted
            join last_tvl on last_tvl.symbol = tvl_weighted.symbol
            left join new_holders on new_holders.symbol = tvl_weighted.symbol
            left join price_delta on price_delta.symbol = tvl_weighted.symbol
        """
        logger.info(f"Generated SQL: {SQL}")

        results: Dict[str, ProjectStat] = {}
        with psycopg2.connect() as pg:
            if dry_run:
                logger.info("Running SQL query in dry_run mode")
                with pg.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                    cursor.execute(f"explain {SQL}")
            else:
                logger.info("Running SQL query in production mode")
                with pg.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cursor:
                    cursor.execute(SQL)
                    for row in cursor.fetchall():
                        logger.info(row)
                        assert row['symbol'] not in results
                        results[row['symbol']] = ProjectStat(
                            name=row['symbol'],
                            metrics={}
                        )
                        results[row['symbol']].metrics[ProjectStat.TOKEN_ADDRESS] = row['address']
                        results[row['symbol']].metrics[ProjectStat.TOKEN_IS_MEME] = row['is_meme']
                        results[row['symbol']].metrics[ProjectStat.TOKEN_HAS_BOOST] = row['has_boost']
                        results[row['symbol']].metrics[ProjectStat.TOKEN_TVL_CHANGE] = int(row['tvl_change'])
                        results[row['symbol']].metrics[ProjectStat.TOKEN_START_TVL] = int(row['start_tvl'])
                        results[row['symbol']].metrics[ProjectStat.TOKEN_LAST_TVL] = int(row['last_tvl'])
                        results[row['symbol']].metrics[ProjectStat.TOKEN_PRICE_BEFORE] = float(row['price_before'])
                        results[row['symbol']].metrics[ProjectStat.TOKEN_PRICE_AFTER] = float(row['price_after'])
                        results[row['symbol']].metrics[ProjectStat.TOKEN_PRICE_CHANGE_NORMED] = float(row['price_delta_normed'])
                        results[row['symbol']].metrics[ProjectStat.TOKEN_PRICE_CHANGE_SIMPLE] = float(row['price_delta'])
                        results[row['symbol']].metrics[ProjectStat.TOKEN_NEW_USERS_WITH_MIN_AMOUNT] = int(row['new_holders'])
                logger.info("Tokens query finished")

        return CalculationResults(ranking=results.values(), build_time=1)  # TODO build time
