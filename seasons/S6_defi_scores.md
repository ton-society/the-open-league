# S6 DeFi Users scores

S6 DeFi consists of two squads: the Volume Squad and the TVL Squad. Each squad has a different scoring system.
Both squads requires explicit enrollement with Degen SBT. SBT Collection address is [EQArE6_3GESQqKwECcgQw-17cuF2_ObtDKqn3-sABG1uuezv](https://tonviewer.com/EQArE6_3GESQqKwECcgQw-17cuF2_ObtDKqn3-sABG1uuezv),
full list of participants could be obtained with the help of [SBTEnrollmentSync](../backends/sbt_enrollment.py).

All queries provided below works with postgres DB produced by [TON-ETL](https://github.com/re-doubt/ton-etl).

## Volume Squad

User score is calculated as a trading volume in any of target projects nominated in USD. Trading volume is calculated
during the period of the season. Methodology details for each projects:

### RainbowSwap

Includes all trades on any dex in case of transaction chain includes a swap with referrall address [UQBBPVrn4Y6F0Fci4j0mXuSAXmRDeE-nZCRIInQsNC9__8vG](https://tonviewer.com/EQBBPVrn4Y6F0Fci4j0mXuSAXmRDeE-nZCRIInQsNC9__5YD).
Volume is estimated for all swaps with TON, staked TON  or USDT according to the methodology from [TON-ETL](https://github.com/re-doubt/ton-etl/blob/main/parser/parsers/message/swap_volume.py).

### GasPump

Volume includes trades extracted from [Gaspump events](https://github.com/re-doubt/ton-etl/blob/main/parser/parsers/message/gaspump.py). USD value is calculated as a product of trade amount and price of TON at the time of trade.


### Tradoor Perps

Volume includes all changes of traders position extracted by [parser](https://github.com/re-doubt/ton-etl/blob/main/parser/parsers/message/tradoor_trades.py). Only events for specific opcodes are taken into account:
* 10 - market order to open or increase position
* 11 - limit order to open or increase position
* 12 - market order to close or decrease position
* 13 - take profit order
* 14 - stop loss order


Full list of volume generating transaction and eligible users could be obtained using the following query:
```sql
with swaps as (
  select  * from parsed.dex_swap_parsed dsp 
  where swap_utime  >= 1726138800 and swap_utime < 1726822800
  and volume_usd > 0
), rainbow_traces as (
  select distinct trace_id from swaps where referral_address =upper('0:413d5ae7e18e85d05722e23d265ee4805e6443784fa764244822742c342f7fff')
), rainbow_swaps as (
  select 'rainbow' as project, tx_hash, swap_user as address, volume_usd from swaps join rainbow_traces using(trace_id)
), tradoor_perps as (
  select 'tradoor' as project, tx_hash, address, size_delta * trigger_price /1e18  / 1e6 as volume_usd from parsed.tradoor_perp_order tpo 
  where event_time  >= 1726138800 and event_time < 1726822800
  and (op_type = 10 or op_type = 11 or op_type = 12 or op_type = 13 or op_type = 14)
), gaspump as (
  select 'gaspump' as project, tx_hash, trader_address, ton_amount /1e9 
  * (select price from prices.ton_price where price_ts < event_time order by price_ts desc limit 1)
  as volume_usd from parsed.gaspump_trade
  where  event_time  >= 1726138800 and event_time < 1726822800
), degens as (
  select distinct address, 1 as degen from tol.enrollment_degen ed 
), volumes as (
  select * from rainbow_swaps
  union all
  select * from tradoor_perps
  union all
  select * from gaspump
)
select * from volumes
```

## TVL Squad

User score is calculated as a total increase of its position locked in all protocols. Initially position
is calulcated in tokens and converted to USD based on the price of the token at the time of the season end.


### JVault

All pools are SBTs from [this collection](https://tonviewer.com/EQAYS3AO2NaFr5-wl1CU8QMiCxrP0OEXYn82iqnuST9FKo9I). 
Each SBT owns one or more jetton masters and all holders of these jettons are 
considered as LPs. Total amount of TVL for each pool is a sum of all tokens and DEX LP tokens owned by this pool.

### SettleTon

All pools are jettons with the same code_hash - ``BfWQzLvuCKusWfxaQs48Xp+Nf+jUIBN8BVrU0li7qXI=``. These
pools are holding DEX LP tokens which are producing TVL. 

###  DAOLama

TVL is amount of TON on [main contract address](https://tonviewer.com/EQCkeTvOSTBwBtP06X2BX7THj_dlX67PhgYRGuKfjWtB9FVb).

### TON Hedge

TVL is amount of TON on [main contract address](https://tonviewer.com/EQBXZo11H4wUq3azWDphoUhlV710a-7rvUsqZUGLP9tUcf37).


Query to get full list of participants and their impact to TVL:
```sql


with jvault_pools as (
 select address as pool_address from nft_items ni where collection_address =upper('0:184b700ed8d685af9fb0975094f103220b1acfd0e117627f368aa9ee493f452a')
), jvault_pool_tvls as (
 select pool_address, 
  coalesce (sum( (select price_usd from prices.agg_prices ap where ap.base = jetton_master and price_time < 1726822800 order by price_time desc limit 1) * balance / 1e6), 0)
  +
  coalesce (sum( (select tvl_usd / total_supply from prices.dex_pool_history dph where pool = jetton_master and timestamp < 1726822800 order by timestamp desc limit 1) * balance), 0)
   as value_usd
   from tol.jetton_wallets_S6_end b
   join jvault_pools p on p.pool_address = b."owner"
   group by 1
), jvault_lp_tokens as (
   select jm.address as lp_master, pool_address from jetton_masters jm join jvault_pools p on p.pool_address =admin_address
), jvault_balances_before as (
 select ed.address, lp_master, balance from tol.jetton_wallets_s6_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join jvault_lp_tokens on lp_master = b.jetton_master
), jvault_balances_after as (
 select ed.address, lp_master, balance from tol.jetton_wallets_s6_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join jvault_lp_tokens on lp_master = b.jetton_master
), jvault_balances_delta as (
 select address, lp_master, coalesce(jvault_balances_after.balance, 0) - coalesce(jvault_balances_before.balance, 0) as balance_delta
 from jvault_balances_after left join jvault_balances_before using(address, lp_master) 
), jvault_total_supply as (
   select lp_master, sum(balance) as total_supply
   from tol.jetton_wallets_s6_end b
   join jvault_lp_tokens on lp_master = b.jetton_master
   group by 1
), jvault_impact as (
 select address, sum(value_usd * balance_delta / total_supply) as tvl_impact from jvault_balances_delta
 join jvault_total_supply using(lp_master)
 join jvault_lp_tokens using(lp_master)
 join jvault_pool_tvls using(pool_address)
 group by 1
), settleton_pools as (
  select address as pool_address from jetton_masters jm where 
  code_hash ='BfWQzLvuCKusWfxaQs48Xp+Nf+jUIBN8BVrU0li7qXI='
), settleton_pool_tvls as (
 select pool_address, 
  coalesce (sum( (select tvl_usd / total_supply from prices.dex_pool_history dph where pool = jetton_master and timestamp < 1726822800 order by timestamp desc limit 1) * balance), 0)
   as value_usd
   from tol.jetton_wallets_S6_end b
   join settleton_pools p on p.pool_address = b."owner"
   group by 1
), settleton_balances_before as (
 select ed.address, pool_address, balance from tol.jetton_wallets_s6_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join settleton_pools on pool_address = b.jetton_master
), settleton_balances_after as (
 select ed.address, pool_address, balance from tol.jetton_wallets_s6_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join settleton_pools on pool_address = b.jetton_master
), settleton_balances_delta as (
 select address, pool_address, coalesce(settleton_balances_after.balance, 0) - coalesce(settleton_balances_before.balance, 0) as balance_delta
 from settleton_balances_after left join settleton_balances_before using(address, pool_address) 
), settleton_total_supply as (
   select pool_address, sum(balance) as total_supply
   from tol.jetton_wallets_s6_end b
   join settleton_pools on pool_address = b.jetton_master
   group by 1
), settleton_impact as (
 select address, sum(value_usd * balance_delta / total_supply) as tvl_impact from settleton_balances_delta
 join settleton_total_supply using(pool_address)
 join settleton_pool_tvls using(pool_address)
 group by 1
), daolama_tvl as (
select balance * (select price from prices.ton_price where price_ts < 1726822800 order by price_ts desc limit 1) / 1e9 as tvl_usd 
from account_states as2 where hash = (
select account_state_hash_after from transactions where account = upper('0:a4793bce49307006d3f4e97d815fb4c78ff7655faecf8606111ae29f8d6b41f4')
and now < 1726822800
order by now desc limit 1)
), daolama_balances_before as (
 select ed.address, balance from tol.jetton_wallets_s6_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 where b.jetton_master = upper('0:a4793bce49307006d3f4e97d815fb4c78ff7655faecf8606111ae29f8d6b41f4')
), daolama_balances_after as (
 select ed.address, balance from tol.jetton_wallets_s6_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 where b.jetton_master = upper('0:a4793bce49307006d3f4e97d815fb4c78ff7655faecf8606111ae29f8d6b41f4')
), daolama_balances_delta as (
 select address, coalesce(daolama_balances_after.balance, 0) - coalesce(daolama_balances_before.balance, 0) as balance_delta
 from daolama_balances_after left join daolama_balances_before using(address)
), daolama_total_supply as (
   select sum(balance) as total_supply
   from tol.jetton_wallets_s6_end b
   where b.jetton_master = upper('0:a4793bce49307006d3f4e97d815fb4c78ff7655faecf8606111ae29f8d6b41f4')
), daolama_impact as (
 select address, sum((select tvl_usd from daolama_tvl) * balance_delta / (select total_supply from daolama_total_supply)) as tvl_impact from daolama_balances_delta
 group by 1
), tonhedge_tvl as (
 select balance / 1e6 as tvl_usd from tol.jetton_wallets_s6_end
 where owner = upper('0:57668d751f8c14ab76b3583a61a1486557bd746beeebbd4b2a65418b3fdb5471')
 and jetton_master = '0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE'
), tonhedge_balances_before as (
 select ed.address, balance from tol.jetton_wallets_s6_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 where b.jetton_master = upper('0:57668d751f8c14ab76b3583a61a1486557bd746beeebbd4b2a65418b3fdb5471')
), tonhedge_balances_after as (
 select ed.address, balance from tol.jetton_wallets_s6_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 where b.jetton_master = upper('0:57668d751f8c14ab76b3583a61a1486557bd746beeebbd4b2a65418b3fdb5471')
), tonhedge_balances_delta as (
 select address, coalesce(tonhedge_balances_after.balance, 0) - coalesce(tonhedge_balances_before.balance, 0) as balance_delta
 from tonhedge_balances_after left join tonhedge_balances_before using(address)
), tonhedge_total_supply as (
   select sum(balance) as total_supply
   from tol.jetton_wallets_s6_end b
   where b.jetton_master = upper('0:57668d751f8c14ab76b3583a61a1486557bd746beeebbd4b2a65418b3fdb5471')
), tonhedge_impact as (
 select address, sum((select tvl_usd from tonhedge_tvl) * balance_delta / (select total_supply from tonhedge_total_supply)) as tvl_impact 
 from tonhedge_balances_delta
 group by 1
), all_projects_impact as (
 select * from jvault_impact
   union all
 select * from settleton_impact
   union all
 select * from daolama_impact
   union all
 select * from tonhedge_impact
)
select address, sum(tvl_impact) as tvl_impact from all_projects_impact
group by 1
```