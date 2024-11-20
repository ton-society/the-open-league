with swaps as (
  select * from parsed.dex_swap_parsed dsp 
  where swap_utime  >= 1732705200 and swap_utime < 1734433200
  and volume_usd > 0
), rainbow_traces as (
  select distinct trace_id from swaps where referral_address =upper('0:413d5ae7e18e85d05722e23d265ee4805e6443784fa764244822742c342f7fff')
), rainbow_swaps as (
  select 'rainbow' as project, tx_hash, swap_user as address, volume_usd from swaps join rainbow_traces using(trace_id)
), rainbow_points as (
  select address, floor(sum(volume_usd) / 20.) * 1 as points from rainbow_swaps
  group by 1
), tondiamonds_swaps as (
  select 'tondiamonds' as project, tx_hash, swap_user as address, volume_usd from swaps where referral_address =upper('0:d9949a2b4a80787112796fc82dd2a4786e42dfcd50d55dee5298c3dc125d1304')
), tondiamonds_points as (
  select address, floor(sum(volume_usd) / 20.) * 1 as points from tondiamonds_swaps
  group by 1
), gaspump as (
  select 'gaspump' as project, tx_hash, trader_address as address, ton_amount /1e9 
  * (select price from prices.ton_price where price_ts < event_time order by price_ts desc limit 1)
  as volume_usd from parsed.gaspump_trade
  where  event_time  >= 1732705200 and event_time < 1734433200
), gaspump_points as (
  select address, floor(sum(volume_usd) / 20.) * 5 as points from gaspump
  group by 1
), degens as (
  select distinct address, 1 as degen from tol.enrollment_degen ed 
), volume_points as (
  select * from rainbow_points
  union all
  select * from gaspump_points
  union all
  select * from tondiamonds_points
)
select address, sum(points) as points from volume_points
join degens using(address)
where points > 0
group by 1