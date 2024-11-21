# S7 DeFi Users scores

S7 DeFi consists of two squads: the Volume Squad and the TVL Squad. Overall user score is a sum of points from both squads.
Minimum amount of volume/TVL and points per each action could be found in the [Points system](#points-system) section.
To be eligible for the competition user has to pass explicit enrollement with Degen SBT. SBT Collection address is [TODO](TODO),
full list of participants could be obtained with the help of [SBTEnrollmentSync](../backends/sbt_enrollment.py).

All queries provided below works with postgres DB produced by [TON-ETL](https://github.com/re-doubt/ton-etl).


## Volume Squad

User score is calculated as a trading volume in any of target projects nominated in USD. Trading volume is calculated
during the period of the season. Minimum amount of volume to be eligible for receiving points is 20 USD.
Methodology details for each projects:

### RainbowSwap

Includes all trades on any dex in case of transaction chain includes a swap with referrall address [UQBBPVrn4Y6F0Fci4j0mXuSAXmRDeE-nZCRIInQsNC9__8vG](https://tonviewer.com/EQBBPVrn4Y6F0Fci4j0mXuSAXmRDeE-nZCRIInQsNC9__5YD).
Volume is estimated for all swaps with TON, staked TON or USDT according to the methodology from [TON-ETL](https://github.com/re-doubt/ton-etl/blob/main/parser/parsers/message/swap_volume.py).

### GasPump

Volume includes trades extracted from [Gaspump events](https://github.com/re-doubt/ton-etl/blob/main/parser/parsers/message/gaspump.py). USD value is calculated as a product of trade amount and price of TON at the time of trade.


Full list of volume generating transaction and eligible users could be obtained using [the following query](sql/s7_defi_volume.sql).


## TVL Squad

User score is calculated as a total increase of its position locked in each protocols. Initially position
is calulcated in tokens and converted to USD based on the price of the token at the time of the season end.
Minimum amount of TVL increase to be eligible for receiving points is 20 USD.

### JVault

All pools are SBTs from [this collection](https://tonviewer.com/EQAYS3AO2NaFr5-wl1CU8QMiCxrP0OEXYn82iqnuST9FKo9I). 
Each SBT owns one or more jetton masters and all holders of these jettons are 
considered as LPs. Total amount of TVL for each pool is a sum of all tokens and DEX LP tokens owned by this pool.

### SettleTon

All pools are jettons, full list of pools provided in the [query](sql/s7_defi_tvl.sql) (see `settleton_pools` CTE).
Also some pools are aggregating TVL from other pools and we aggregating its TVL into single pool.
The pools are holding DEX LP tokens which are producing TVL. 

### Parraton

All pools are jettons with the same admin address - [EQBwWldOF2pHx4XM6CHlwdxVG6ZfcOgokT767236ZIGE5hKI](https://tonviewer.com/EQBwWldOF2pHx4XM6CHlwdxVG6ZfcOgokT767236ZIGE5hKI). These
pools are holding DEX LP tokens which are producing TVL. 

###  DAOLama

Total TVL is amount of TON on [main contract address](https://tonviewer.com/EQCkeTvOSTBwBtP06X2BX7THj_dlX67PhgYRGuKfjWtB9FVb).
Main contract also serves as a LP token.

### TON Hedge

TVL is amount of USDT on [main contract address](https://tonviewer.com/EQBXZo11H4wUq3azWDphoUhlV710a-7rvUsqZUGLP9tUcf37).
Main contract also serves as a LP token.

### TON Pools

TVL originated from deposits and decreased by withdrawals. Deposits are messages with opcode 0x21eeb607 to [tonpools.ton](https://tonviewer.com/EQA7y9QkiP4xtX_BhOpY4xgVlLM7LPcYUA4QhBHhFZeL4fTa), withdrawals are messages with opcode 0x0ba69751 to [tonpools.ton](https://tonviewer.com/EQA7y9QkiP4xtX_BhOpY4xgVlLM7LPcYUA4QhBHhFZeL4fTa) followed by "Withdraw completed" response message which carries amount of TON to withdraw.

### TON Stable

TVL originated after tsTON/stTON deposits, so it is a sum of all tsTON/stTON transfers by the users to 
[the project smart-contract](https://tonviewer.com/EQC2Bt4vwcSgCwABlOfgl75GbGuC0GpRU2GsZKqqMHu-T0gk)

### Aqua Protocol

TVL originated after tsTON/stTON/hTON deposits, so it is a sum of all tsTON/stTON/hTON transfers by the users to 
[the project smart-contract](https://tonviewer.com/EQAWDyxARSl3ol2G1RMLMwepr3v6Ter5ls3jiAlheKshgg0K)


Full list of participants and their impact on TVL could be obtained by [this query](sql/s7_defi_tvl.sql).


## Points system

|DeFi Protocol name | Squad | Points per each 20 USD|
|:-|:-|-:|
|Rainbow Swap|Volume|1|
|DEX Diamonds|Volume|1|
|GasPump|Volume|5|
|Aqua protocol|TVL|15|
|JVault|TVL|10|
|DAOLama|TVL|15|
|Parraton|TVL|10|
|SettleTON|TVL|10|
|TonPools|TVL|10|
|TonStable|TVL|15|
|TON Hedge|TVL|10|