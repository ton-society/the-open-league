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
* [Before the break](sql/s6_part1_defi_volume.sql)
* [After the break](sql/s6_part2_defi_volume.sql)


## TVL Squad

User score is calculated as a total increase of its position locked in all protocols. Initially position
is calulcated in tokens and converted to USD based on the price of the token at the time of the season end.


### JVault

All pools are SBTs from [this collection](https://tonviewer.com/EQAYS3AO2NaFr5-wl1CU8QMiCxrP0OEXYn82iqnuST9FKo9I). 
Each SBT owns one or more jetton masters and all holders of these jettons are 
considered as LPs. Total amount of TVL for each pool is a sum of all tokens and DEX LP tokens owned by this pool.

### SettleTon

All pools are jettons but it is impossible to get the list of pools by code_hash because
there were updates during the season. So we are using explicit list of pools hard-coded in the query.
Also some pools are aggregating TVL from other pools and we aggregating its TVL into single pool.
The pools are holding DEX LP tokens which are producing TVL. 

### Parraton

All pools are jettons with the same admin address - [EQBwWldOF2pHx4XM6CHlwdxVG6ZfcOgokT767236ZIGE5hKI](https://tonviewer.com/EQBwWldOF2pHx4XM6CHlwdxVG6ZfcOgokT767236ZIGE5hKI). These
pools are holding DEX LP tokens which are producing TVL. 

###  DAOLama

TVL is amount of TON on [main contract address](https://tonviewer.com/EQCkeTvOSTBwBtP06X2BX7THj_dlX67PhgYRGuKfjWtB9FVb).

### TON Hedge

TVL is amount of TON on [main contract address](https://tonviewer.com/EQBXZo11H4wUq3azWDphoUhlV710a-7rvUsqZUGLP9tUcf37).

### TON Pools

TVL originated from deposits and decreased by withdrawals. Deposits are messages with opcode 0x21eeb607 to [tonpools.ton](https://tonviewer.com/EQA7y9QkiP4xtX_BhOpY4xgVlLM7LPcYUA4QhBHhFZeL4fTa), withdrawals are messages with opcode 0x0ba69751 to [tonpools.ton](https://tonviewer.com/EQA7y9QkiP4xtX_BhOpY4xgVlLM7LPcYUA4QhBHhFZeL4fTa) followed by "Withdraw completed" response message which carries amount of TON to withdraw.

### TON Stable

TVL originated after tsTON/stTON deposits, so it is a sum of all tsTON/stTON transfers by the users to 
[the project smart-contract](https://tonviewer.com/EQC2Bt4vwcSgCwABlOfgl75GbGuC0GpRU2GsZKqqMHu-T0gk)

### Aqua Protocol

TVL originated after tsTON/stTON/hTON deposits, so it is a sum of all tsTON/stTON/hTON transfers by the users to 
[the project smart-contract](https://tonviewer.com/EQAWDyxARSl3ol2G1RMLMwepr3v6Ter5ls3jiAlheKshgg0K)

### TonStakers

TVL impact is calculated as an increase of token position by transfers to specific staking NFT collections.
The list of tokens and collections is present in [here](https://github.com/DefiLlama/DefiLlama-Adapters/blob/5f2f78df1b47fd064ac72ec384564860c63f63c4/projects/tonstakers-token-staking/index.js#L41).


Queries to get full list of participants and their impact to TVL are available in [sql](sql/) folder:
* [Before the break](sql/s6_part1_defi_tvl.sql)
* [After the break](sql/s6_part2_defi_tvl.sql)