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
 select address, floor(sum(value_usd * balance_delta / total_supply) / 20.) * 10 as tvl_impact from jvault_balances_delta
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
 select address, floor(sum((select tvl_usd from daolama_tvl) * balance_delta / (select total_supply from daolama_total_supply)) / 20.) * 15 as tvl_impact from daolama_balances_delta
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
  select address, floor(sum(tvl_usd) / 20.) * 10 as tvl_impact from swapcoffee_flow
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
), all_projects_degen_only as (
select p.* from all_projects_impact p
join tol.enrollment_degen ed on ed.address = p.address
)
select address, sum(tvl_impact) as points from all_projects_degen_only
where tvl_impact > 0
group by 1