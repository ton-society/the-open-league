with wallets_start as (
  select distinct on(address) address, tx_lt, jetton_master, "owner", balance from parsed.jetton_wallet_balances 
  where tx_lt < 51063176000000 -- TODO change to start of season 
  order by address, tx_lt desc
), wallets_end as (
  select address, last_transaction_lt as tx_lt, jetton as jetton_master, "owner", balance from jetton_wallets
), jvault_pools as (
 select address as pool_address from nft_items ni where collection_address =upper('0:184b700ed8d685af9fb0975094f103220b1acfd0e117627f368aa9ee493f452a')
), jvault_pool_tvls as (
 select pool_address, 
  coalesce (sum( (select price_usd from prices.agg_prices ap where ap.base = jetton_master and price_time < 1734433200 order by price_time desc limit 1) * balance / 1e6), 0)
  +
  coalesce (sum( (select tvl_usd / total_supply from prices.dex_pool_history dph where pool = jetton_master and timestamp < 1734433200 order by timestamp desc limit 1) * balance), 0)
   as value_usd
   from wallets_end b
   join jvault_pools p on p.pool_address = b."owner"
   group by 1
), jvault_lp_tokens as (
   select jm.address as lp_master, pool_address from jetton_masters jm join jvault_pools p on p.pool_address =admin_address
), jvault_balances_before as (
 select ed.address, lp_master, balance from wallets_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join jvault_lp_tokens on lp_master = b.jetton_master
), jvault_balances_after as (
 select ed.address, lp_master, balance from wallets_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join jvault_lp_tokens on lp_master = b.jetton_master
), jvault_balances_delta as (
 select address, lp_master, coalesce(jvault_balances_after.balance, 0) - coalesce(jvault_balances_before.balance, 0) as balance_delta
 from jvault_balances_after left join jvault_balances_before using(address, lp_master) 
), jvault_total_supply as (
   select lp_master, sum(balance) as total_supply
   from wallets_end b
   join jvault_lp_tokens on lp_master = b.jetton_master
   group by 1
   having sum(balance) > 0
), jvault_impact as (
 select address, floor(sum(value_usd * balance_delta / total_supply) / 20.) * 5 as tvl_impact from jvault_balances_delta
 join jvault_total_supply using(lp_master)
 join jvault_lp_tokens using(lp_master)
 join jvault_pool_tvls using(pool_address)
 group by 1
), settleton_pools as (
  select upper('0:64216a0ead5819dca7d1719fc912cfa6673665a1c5fcf7338ca5b2ce65f12f80') as pool_address
  union all
  select upper('0:9be109c3d18d14d6f271f1c311831aef109c2f02062f504726af26ba707f0292') as pool_address
  union all
  select upper('0:f26a93829fdf8448a4ed3cce22a7c92433be18fb668e63cf048a96c5b27fffaa') as pool_address
  union all
  select upper('0:ab9d7bda5f91c06fc3cf737acfed24b63080a65db1b5e95400d503a24c047ed5') as pool_address
  union all
  select upper('0:3848b9a49c1d1a8e9c7101e5a3a80a5638ba968d52882bf34ef4c8eb4090cc60') as pool_address
  union all
  select upper('0:56f5e805e4e407d61a20ad94c83e3aaefa0854be28c633f658aca4c679f8c5e7') as pool_address
  union all
  select upper('0:dacaea937930943b921d18c34da7ed31d95c5ec17948b2246554b2c6422b2747') as pool_address
  union all
  select upper('0:5b46607213a02eec4061be961e41f69a6bfdb4ccb56b2a7ae5d38d25b42eff1d') as pool_address
), settleton_pool_tvls as (
 select pool_address, 
  coalesce (sum( (select tvl_usd / total_supply from prices.dex_pool_history dph where pool = jetton_master and timestamp < 1734433200 order by timestamp desc limit 1) * balance), 0)
   as value_usd
   from wallets_end b
   join settleton_pools p on p.pool_address = b."owner"
   group by 1
), settleton_balances_before as (
 select ed.address, pool_address, balance from wallets_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join settleton_pools on pool_address = b.jetton_master
), settleton_balances_after as (
 select ed.address, pool_address, balance from wallets_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join settleton_pools on pool_address = b.jetton_master
), settleton_balances_delta as (
 select address, pool_address, coalesce(settleton_balances_after.balance, 0) - coalesce(settleton_balances_before.balance, 0) as balance_delta
 from settleton_balances_after left join settleton_balances_before using(address, pool_address) 
), settleton_total_supply as (
   select pool_address, sum(balance) as total_supply
   from wallets_end b
   join settleton_pools on pool_address = b.jetton_master
   group by 1
   having sum(balance) > 0
), settleton_index_pools as (
 select p.pool_address, balance * tvls.value_usd / supply.total_supply
   as value_usd
   from wallets_end b
   join settleton_pools p on p.pool_address = b."owner"
   join settleton_pool_tvls tvls on tvls.pool_address = b.jetton_master
   join settleton_total_supply supply on supply.pool_address = tvls.pool_address
--   group by 1
), settleton_pools_tvl_2_flat as (
 select pool_address, value_usd from settleton_pool_tvls
union all
select pool_address, value_usd from settleton_index_pools
), settleton_pools_tvl_2 as (
 select pool_address, sum(value_usd) as value_usd from settleton_pools_tvl_2_flat
 group by 1
), settleton_impact as (
 select address, floor(sum(value_usd * balance_delta / total_supply) / 20.) * 10 as tvl_impact from settleton_balances_delta
 join settleton_total_supply using(pool_address)
 join settleton_pools_tvl_2 using(pool_address)
 group by 1
), daolama_tvl as (
select balance * (select price from prices.ton_price where price_ts < 1734433200 order by price_ts desc limit 1) / 1e9 as tvl_usd 
from account_states as2 where hash = (
select account_state_hash_after from transactions where account = upper('0:a4793bce49307006d3f4e97d815fb4c78ff7655faecf8606111ae29f8d6b41f4')
and now < 1734433200
order by now desc limit 1)
), daolama_balances_before as (
 select ed.address, balance from wallets_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 where b.jetton_master = upper('0:a4793bce49307006d3f4e97d815fb4c78ff7655faecf8606111ae29f8d6b41f4')
), daolama_balances_after as (
 select ed.address, balance from wallets_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 where b.jetton_master = upper('0:a4793bce49307006d3f4e97d815fb4c78ff7655faecf8606111ae29f8d6b41f4')
), daolama_balances_delta as (
 select address, coalesce(daolama_balances_after.balance, 0) - coalesce(daolama_balances_before.balance, 0) as balance_delta
 from daolama_balances_after left join daolama_balances_before using(address)
), daolama_total_supply as (
   select sum(balance) as total_supply
   from wallets_end b
   where b.jetton_master = upper('0:a4793bce49307006d3f4e97d815fb4c78ff7655faecf8606111ae29f8d6b41f4')
), daolama_impact as (
 select address, floor(sum((select tvl_usd from daolama_tvl) * balance_delta / (select total_supply from daolama_total_supply)) / 20.) * 10 as tvl_impact from daolama_balances_delta
 group by 1
), tonhedge_tvl as (
 select balance / 1e6 as tvl_usd from wallets_end
 where owner = upper('0:57668d751f8c14ab76b3583a61a1486557bd746beeebbd4b2a65418b3fdb5471')
 and jetton_master = '0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE'
), tonhedge_balances_before as (
 select ed.address, balance from wallets_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 where b.jetton_master = upper('0:57668d751f8c14ab76b3583a61a1486557bd746beeebbd4b2a65418b3fdb5471')
), tonhedge_balances_after as (
 select ed.address, balance from wallets_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 where b.jetton_master = upper('0:57668d751f8c14ab76b3583a61a1486557bd746beeebbd4b2a65418b3fdb5471')
), tonhedge_balances_delta as (
 select address, coalesce(tonhedge_balances_after.balance, 0) - coalesce(tonhedge_balances_before.balance, 0) as balance_delta
 from tonhedge_balances_after left join tonhedge_balances_before using(address)
), tonhedge_total_supply as (
   select sum(balance) as total_supply
   from wallets_end b
   where b.jetton_master = upper('0:57668d751f8c14ab76b3583a61a1486557bd746beeebbd4b2a65418b3fdb5471')
), tonhedge_impact as (
 select address, floor(sum((select tvl_usd from tonhedge_tvl) * balance_delta / (select total_supply from tonhedge_total_supply)) / 20.) * 10 as tvl_impact 
 from tonhedge_balances_delta
 group by 1
), tonpools_operations as (
  select source as address, value / 1e9 * 
  (select price from prices.ton_price where price_ts < m.created_at order by price_ts desc limit 1) as value_usd
  from messages m where direction ='in' and destination =upper('0:3bcbd42488fe31b57fc184ea58e3181594b33b2cf718500e108411e115978be1')
  and created_at >= 1732705200 and created_at < 1734433200 and opcode = 569292295
   union all
  select m_in.source as address, -1 * m_out.value  / 1e9 *
  (select price from prices.ton_price where price_ts < m_out.created_at order by price_ts desc limit 1) as value_usd
  from messages m_in
  join messages m_out on m_out.tx_hash  = m_in.tx_hash and m_out.direction  = 'out'
  join parsed.message_comments mc on mc.hash  = m_out.body_hash 
  where m_in.direction ='in' and m_in.destination =upper('0:3bcbd42488fe31b57fc184ea58e3181594b33b2cf718500e108411e115978be1')
  and m_in.created_at  >= 1732705200 and m_in.created_at < 1734433200 and m_in.opcode = 195467089
  and mc."comment" = 'Withdraw completed'
), tonpools_impact as (
 select address, floor(sum(value_usd) / 20.) * 10 as tvl_impact
 from tonpools_operations group by 1
), parraton_pools as (
  select address as pool_address from jetton_masters jm where 
  admin_address = '0:705A574E176A47C785CCE821E5C1DC551BA65F70E828913EFAEF6DFA648184E6'
), parraton_pool_tvls as (
 select pool_address, 
  coalesce (sum( (select tvl_usd / total_supply from prices.dex_pool_history dph where pool = jetton_master and timestamp < 1734433200 order by timestamp desc limit 1) * balance), 0)
   as value_usd
   from wallets_end b
   join parraton_pools p on p.pool_address = b."owner"
   group by 1
), parraton_balances_before as (
 select ed.address, pool_address, balance from wallets_start b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join parraton_pools on pool_address = b.jetton_master
), parraton_balances_after as (
 select ed.address, pool_address, balance from wallets_end b
 join tol.enrollment_degen ed on ed.address = b."owner"
 join parraton_pools on pool_address = b.jetton_master
), parraton_balances_delta as (
 select address, pool_address, coalesce(parraton_balances_after.balance, 0) - coalesce(parraton_balances_before.balance, 0) as balance_delta
 from parraton_balances_after left join parraton_balances_before using(address, pool_address) 
), parraton_total_supply as (
   select pool_address, sum(balance) as total_supply
   from wallets_end b
   join parraton_pools on pool_address = b.jetton_master
   group by 1
  having sum(balance) > 0
), parraton_impact as (
 select address, floor(sum(value_usd * balance_delta / total_supply) / 20.) * 10 as tvl_impact from parraton_balances_delta
 join parraton_total_supply using(pool_address)
 join parraton_pool_tvls using(pool_address)
 group by 1
), tonstable_flow as (
  select 
  case when destination = upper('0:b606de2fc1c4a00b000194e7e097be466c6b82d06a515361ac64aaaa307bbe4f') then source
  else destination end as address,
  case when source = upper('0:b606de2fc1c4a00b000194e7e097be466c6b82d06a515361ac64aaaa307bbe4f') then -1 else 1 end * amount / 1e9 * 
  coalesce((select price from prices.core where asset = jetton_master_address and price_ts < tx_now order by price_ts desc limit 1), 1) *
  (select price from prices.ton_price where price_ts < tx_now order by price_ts desc limit 1) as tvl_usd
  from jetton_transfers
  where (jetton_master_address = upper('0:cd872fa7c5816052acdf5332260443faec9aacc8c21cca4d92e7f47034d11892') 
  or jetton_master_address = upper('0:bdf3fa8098d129b54b4f73b5bac5d1e1fd91eb054169c3916dfc8ccd536d1000'))
  and tx_now  >= 1732705200 and tx_now < 1734433200 
  and (
    destination = upper('0:b606de2fc1c4a00b000194e7e097be466c6b82d06a515361ac64aaaa307bbe4f')
  or
    source = upper('0:b606de2fc1c4a00b000194e7e097be466c6b82d06a515361ac64aaaa307bbe4f')
  ) and not tx_aborted
), tonstable_impact as (
  select address, floor(sum(tvl_usd) / 20.) * 15 as tvl_impact from tonstable_flow
  group by 1
), aqua_flow as (
  select 
  case when destination = upper('0:160f2c40452977a25d86d5130b3307a9af7bfa4deaf996cde388096178ab2182') then source
  else destination end as address,
  case when source = upper('0:160f2c40452977a25d86d5130b3307a9af7bfa4deaf996cde388096178ab2182') then -1 else 1 end * amount / 1e9 * 
  coalesce((select price from prices.core where asset = jetton_master_address and price_ts < tx_now order by price_ts desc limit 1), 1) *
  (select price from prices.ton_price where price_ts < tx_now order by price_ts desc limit 1) as tvl_usd
  from jetton_transfers
  where (jetton_master_address = upper('0:cd872fa7c5816052acdf5332260443faec9aacc8c21cca4d92e7f47034d11892') 
  or jetton_master_address = upper('0:bdf3fa8098d129b54b4f73b5bac5d1e1fd91eb054169c3916dfc8ccd536d1000')
  or jetton_master_address = upper('0:cf76af318c0872b58a9f1925fc29c156211782b9fb01f56760d292e56123bf87')
  )
  and tx_now  >= 1732705200 and tx_now < 1734433200 
  and (
    destination = upper('0:160f2c40452977a25d86d5130b3307a9af7bfa4deaf996cde388096178ab2182')
  or
    source = upper('0:160f2c40452977a25d86d5130b3307a9af7bfa4deaf996cde388096178ab2182')
  ) and not tx_aborted
), aqua_impact as (
  select address, floor(sum(tvl_usd) / 20.) * 15 as tvl_impact from aqua_flow
  group by 1
), swapcoffee_jettons as (
  select upper('0:a5d12e31be87867851a28d3ce271203c8fa1a28ae826256e73c506d94d49edad') as jetton_master_address
  union all
  select upper('0:123e245683bd5e93ae787764ebf22291306f4a3fcbb2dcfcf9e337186af92c83') as jetton_master_address
  union all
  select upper('0:6a839f7a9d6e5303d71f51e3c41469f2c35574179eb4bfb420dca624bb989753') as jetton_master_address
), swapcoffee_flow as (
  select "source" as address,
  case
    when jetton_master_address = upper('0:a5d12e31be87867851a28d3ce271203c8fa1a28ae826256e73c506d94d49edad') then
      coalesce((select price_usd from prices.agg_prices ap where ap.base = jetton_master_address and price_time < 1734433200 order by price_time desc limit 1) * jt.amount / 1e6, 0)
    else
      coalesce((select jt.amount * tvl_usd / total_supply from prices.dex_pool_history dph where pool = jetton_master_address and "timestamp" < 1734433200 order by "timestamp" desc limit 1), 0)
  end as tvl_usd
  from jetton_transfers jt 
  join swapcoffee_jettons using(jetton_master_address)
  where destination = upper('0:29f90533937d696105883b981e9427d1ae411eef5b08eab83f4af89c495d27df')
  and not tx_aborted
  and tx_now >= 1732705200 and tx_now < 1734433200
), swapcoffee_impact as (
  select address, floor(sum(tvl_usd) / 20.) * 5 as tvl_impact from swapcoffee_flow
  group by 1
), coffin_assets as (
  select 'TON' as symbol,
  '0:1A4219FE5E60D63AF2A3CC7DCE6FEC69B45C6B5718497A6148E7C232AC87BD8A' as asset_id,
  '0:0000000000000000000000000000000000000000000000000000000000000000' as jetton_address
  union all
  select 'USDT' as symbol,
  '0:CA9006BD3FB03D355DAEEFF93B24BE90AFAA6E3CA0073FF5720F8A852C933278' as asset_id,
  '0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE' as jetton_address
  union all
  select 'HYDRA' as symbol,
  '0:EC96F4CFD28C381277B7A2A796F0FF91DC8D93ECDDF9C8E8D570473B5900BCDD' as asset_id,
  '0:F83F7D94D74B2736821ABE8ABA7183D3411F367B00233B6D1EA6282B59102EA7' as jetton_address
  union all
  select 'GRAM' as symbol,
  '0:EA9873AB493D0C43D24D89EE1F96080B91521D3C6AE0E0199A673FFEF92E2021' as asset_id,
  '0:B8EF4F77A17E5785BD31BA4DA50ABD91852F2B8FEBEE97AD6EE16D941F939198' as jetton_address
  union all
  select 'ANON' as symbol,
  '0:6E0DB23E574A1AB873107C341EFBC5FA22616D3EECB1CECFAC12B9D22589C203' as asset_id,
  '0:EFFB2AF8D7F099DAEAE0DA07DE8157DAE383C33E320AF45F8C8A510328350886' as jetton_address
  union all
  select 'durev' as symbol,
  '0:5FF06029CA6BABEDB1633E6081A63944086058E3DD3681FDE6F292729B14B096' as asset_id,
  '0:74D8327471D503E2240345B06FE1A606DE1B5E3C70512B5B46791B429DAB5EB1' as jetton_address
), coffin_prices as (
  select asset_id, 
  case 
  	when symbol = 'TON' then (select price from prices.ton_price p where p.price_ts < 1734433200 order by price_ts desc limit 1) / 1e3
  	when symbol = 'USDT' then 1
  	else (select price_usd from prices.agg_prices ap 
  	  where ap.base = jetton_address and price_time < 1734433200 order by price_time desc limit 1)
  end as price
  from coffin_assets
), coffin_events as (
  select tx_hash, owner_address as address, asset_id, amount from parsed.evaa_supply es
  where pool_address = '0:68CF02950F26BD20BDCAC38991E40429878CA8D7912E31DC97F272E58DE694C6'
  and utime >= 1732705200 and utime < 1734433200
  union all 
  select tx_hash, owner_address, asset_id, -amount from parsed.evaa_withdraw ew
  where pool_address = '0:68CF02950F26BD20BDCAC38991E40429878CA8D7912E31DC97F272E58DE694C6'
  and utime >= 1732705200 and utime < 1734433200
), coffin_totals as (
  select address, asset_id, sum(amount * price / 1e6) as volume_usd
  from coffin_events
  join coffin_prices using (asset_id)
  group by 1, 2
), coffin_impact as (
  select address, floor(sum(volume_usd) / 20.) * 10 as tvl_impact
  from coffin_totals
  group by 1
),
-- TONCO
tonco_collections as (
  -- get all NFT pools owner by the router
  select  address from public.nft_collections nc where 
  owner_address ='0:BFFADD270A738531DA7B13BA8FC403826C2586173F9EDE9C316FAB53BC59AC86'
), tonco_positions as (
  -- get all NFT positions which is active now (init=true)
  select address, owner_address from public.nft_items ni 
  where collection_address in (select * from tonco_collections) and init
), tonco_positions_first_tx as (
  -- get first transaction for every NFT position. This tx will be a part of mint tx chain
  -- to get the first transaction we will filter by end_status and orig_status and also filter 
  -- on the season period, so mints out of the season time range will be nulls
  select *, (select trace_id from transactions t where t.account = p.address and orig_status != 'active' 
  and end_status = 'active' 
  and now > 1732705200 and
  and now < 1734433200
  order by lt asc limit 1) from tonco_positions p
), jetton_transfers as (
  -- now we need to get all liquidity transfers from the LP owner in the same tx chain (trace_id)
  -- so let's take all successful jetton transfers with the same trace_id
  select p.owner_address, p.trace_id, jt.amount, jt.jetton_master_address, tx_now from public.jetton_transfers jt 
  join tonco_positions_first_tx p on p.trace_id = jt.trace_id and p.owner_address = jt.source
  where p.trace_id is not null -- filter out mints outside of the season time range
  and not jt.tx_aborted
), jetton_liquidity_transfers as (
  -- estimate liquidity amount in USD
  select owner_address, trace_id, (
  case
  -- special case - USDT, always 1$
  when jetton_master_address = '0:B113A994B5024A16719F69139328EB759596C38A25F59028B146FECDC3621DFE' 
      then 1
    -- for all other jettons let's get latest agg price just before the event
    else (select price_usd from prices.agg_prices ap where 
        ap.base = jetton_master_address and
        price_time < tx_now
        order by price_time desc limit 1)
  end
  ) * amount / 1e6 as amount_usd from jetton_transfers
), unique_traces as (
  -- prepare all unique traces
  select distinct owner_address, trace_id from jetton_liquidity_transfers
),
pton_transfers as (
  -- unfortunately, wrapped TON by TONCO doesn't comply with TEP-74 and it is missing from the previous filter.
  -- so to get it we will extract all 0x01f3835d messages (pTON) from the same tx chain (the same trace_id)
  -- each messages carries some gas amount (~0.5TON) so we will substract it from the message value
  select owner_address, trace_id, 
  (
    select (greatest(0, value - 5e8)) / 1e9 * (select price from prices.ton_price tp where 
      tp.price_ts < m.created_at order by tp.price_ts desc limit 1) 
    as amount_usd  from trace_edges te -- using trace_adges to get all messages
    join messages m  on m.tx_hash  =te.left_tx and direction = 'in'
    where te.trace_id = unique_traces.trace_id 
  and opcode = 32736093 -- 0x01f3835d
  ) as amount_usd
  from unique_traces
), liquidity_transfers as (
  -- combine jettons and TON transfers
  select owner_address, amount_usd from pton_transfers where amount_usd is not null
  union all
  select owner_address, amount_usd from jetton_liquidity_transfers where amount_usd is not null
), tonco_impact as (
  -- final calculation of impact
  select owner_address as address, floor(sum(amount_usd) / 20.) * 10 as tvl_impact
  from liquidity_transfers group by 1
), farmix_pools as (
  select upper('0:be8e55fcdc36198125915b9abf5ee1cb5961503e9db11a673c042a1e59c90aa5') as pool, -- pTON pool
    upper('0:1bb30d579441ffdbc4f3ab248a460cd748e2a9f044dc0d59ba7871da31648268') as jetton,
    (select price from prices.ton_price p where p.price_ts < 1734433200 order by price_ts desc limit 1) / 1e3 as price
  union all
  select upper('0:fa81049609ac8787416f5274d79697e2cc85a2abb51e138818bd7198b4484860') as pool, -- USDT pool
    upper('0:b113a994b5024a16719f69139328eb759596c38a25f59028b146fecdc3621dfe') as jetton,
    1 as price
  union all
  select upper('0:84ffa4debca1298fc393cf7ad9b750f96d1e9f10d41b48dd9b6d6d23cf16d618') as pool, -- NOT pool
    upper('0:2f956143c461769579baef2e32cc2d7bc18283f40d20bb03e432cd603ac33ffc') as jetton,
    (select price_usd from prices.agg_prices ap 
    where ap.base = upper('0:2f956143c461769579baef2e32cc2d7bc18283f40d20bb03e432cd603ac33ffc') and price_time < 1734433200 
    order by price_time desc limit 1) as price
), farmix_agg_mints as (
  select fp.pool, jt."source" as address, sum(jt.amount) as total_transfer_amount, sum(jm.amount) as total_mint_amount, fp.price
  from parsed.jetton_mint jm
  join farmix_pools fp on jetton_master_address = pool
  join jetton_transfers jt on jm.trace_id = jt.trace_id and jt.destination = fp.pool and jt.jetton_master_address = fp.jetton and not jt.tx_aborted
  where jm.utime >= 1732705200 and jm.utime < 1734433200 and jm.successful
  group by fp.pool, jt."source", fp.price
), farmix_agg_burns as (
  select pool, "owner" as address, sum(amount) as total_burn_amount from jetton_burns jb 
  join farmix_pools fp on jetton_master_address = pool
  where tx_now >= 1732705200 and tx_now < 1734433200 and not tx_aborted
  group by pool, "owner"
), farmix_impact as (
  select address, floor(sum((total_mint_amount - coalesce(total_burn_amount, 0)) / total_mint_amount * total_transfer_amount * price / 1e6) / 20.) * 10 as tvl_impact 
  from farmix_agg_mints
  left join farmix_agg_burns using (pool, address)
  group by 1
), all_projects_impact as (
 select 'jVault' as project, * from jvault_impact
   union all
 select 'SettleTon' as project, * from settleton_impact
   union all
 select 'DAOLama' as project, * from daolama_impact
   union all
 select 'TONHedge' as project, * from tonhedge_impact
   union all
 select 'TONPools' as project, * from tonpools_impact
   union all
 select 'Parraton' as project, * from parraton_impact
   union all
 select 'TONStable' as project, * from tonstable_impact
   union all
 select 'Aqua' as project, * from aqua_impact
   union all
 select 'swap.coffee' as project, * from swapcoffee_impact
   union all
 select 'Coffin' as project, * from coffin_impact
   union all
 select 'TONCO' as project, * from tonco_impact
   union all
 select 'Farmix' as project, * from farmix_impact
), all_projects_degen_only as (
select p.* from all_projects_impact p
join tol.enrollment_degen ed on ed.address = p.address
)
select address, sum(tvl_impact) as points from all_projects_degen_only
where tvl_impact > 0
group by 1