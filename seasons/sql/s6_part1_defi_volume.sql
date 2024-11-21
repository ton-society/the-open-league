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
select address, sum(volume_usd) as volume_usd from volumes
join degens using(address)
group by 1