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

TODO