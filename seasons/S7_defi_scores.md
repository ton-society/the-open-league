# S7 DeFi Users scores

S7 DeFi consists of two squads: the Volume Squad and the TVL Squad. Overall user score is a sum of points from both squads.
Minimum amount of volume/TVL and points per each action could be found in the [Points system](#points-system) section.
To be eligible for the competition user has to pass explicit enrollement with Degen SBT. SBT Collection address is [TODO](TODO),
full list of participants could be obtained with the help of [SBTEnrollmentSync](../backends/sbt_enrollment.py).

All queries provided below works with postgres DB produced by [TON-ETL](https://github.com/re-doubt/ton-etl).


## Volume Squad

User score is calculated as a trading volume in any of target projects nominated in USD. Trading volume is calculated
during the period of the season. Minimum amount of volume to be eligible for receiving points is 20 USD.
For trading volume in pools with low fees a reduction factor of 0.1 is applied since Fri Dec 06 2024 14:30:00 GMT:
* [NIKO/pTON](https://app.ston.fi/pools/EQAGUk1UZNw4etyy2Y3Lacii_u18RUPPaw_s5FLV6yMsatly)
* [tsTON/TON](https://app.ston.fi/pools/EQC_OxV6MQ6csZXNk2Zu6jMrsGRI6m4YRzL2McKaPCYmNk6l)
* [AquaUSD/USDT](https://app.ston.fi/pools/EQDmFQFfmQHA2zril2F3yQswZAYc-k1hN6CK0il1izLe2892)
* [AquaUSD/USDT](https://dedust.io/pools/EQBGCoxXu8a_CdJ5r1u2iiWUvJAAHvVU7qZgEmfKRSfBf2CW)
* [stTON/TON](https://dedust.io/pools/EQCHFiQM_TTSIiKhUCmWSN4aPSTqxJ4VSBEyDFaZ4izyq95Y)
* [wsTON/TON](https://dedust.io/pools/EQABt8YegyD7VJnZdFVwom8wwqp0E0X8tN2Y6NhrDmbrnSXP)
* [DONE/USDT](https://dedust.io/pools/EQBA-CMqyAbvW1pcoEzpEIrPQG4RDY2iq0BLXJx1m1-Ni3ON)

Methodology details for each projects:

### Rainbow.ag

Volume is estimated for all swaps with TON, staked TON or USDT according to the methodology from [TON-ETL](https://github.com/re-doubt/ton-etl/blob/main/parser/parsers/message/swap_volume.py).
Includes all trades on any dex in case of transaction chain includes a swap with referrall address from list:
* UQBBPVrn4Y6F0Fci4j0mXuSAXmRDeE-nZCRIInQsNC9__8vG
* UQDscgosGjQeAfyL1m6-57O5_NusTGYFVDesaB0CkEvo_m4g
* UQCIOI01FJKvUHqUNF-c1BGytouH5HdeOPHCgyk2ddK1Y8oZ
* UQAaCGsY1S7OIonBkom2lOwx6cBMggGKKHukC_n6aq00Q8Tb

### GasPump

Volume includes trades extracted from [Gaspump events](https://github.com/re-doubt/ton-etl/blob/main/parser/parsers/message/gaspump.py). USD value is calculated as a product of trade amount and price of TON at the time of trade.

### swap.coffee

The same methodology as for Rainbow.ag, but with list of referral addresses:
* UQCZ_pV6EJNSr6XpvPaa-IVkT6ImqkiPftRMOICJP1B_78Hc
* UQA8OiygwLotKehQvp285LjTvVsTj6OuHZxEDxxTo6PlJWYA
* UQCoFIQulMX1WciLYp7PUrxFqzIfsaUNo_FLDy1nDD0akyqT
* UQCo2ftIP6_GV9D1BPEctJmrSpyWE0i7Duv9VUKrUgKb-ycW
* UQAZoipwVLWfqgIklSmsKRbmRn-SOHlddH7L6MStlrP1hqTY
* UQD_uBfQr0Rr2_gbBVlDEgCb6CJ-dkoTKs7RCKeZytffxVY6
* UQCyW2VKRoUcVUXl9pc9AV5prdrQa97MMUr5tNNvDtEh6tEy
* UQBVdtzxVLDvdK4MO5goiNeGXJ4m0fsD38u2bo_99_yKN4zK
* UQCboL33t5GC9A8QDbxP7wqR0hIVOhDmAQwD0nJWC2e6T17t
* UQDpBMtznS0tXtOsh-dHbCkdp49Reh96JHxitxDSLPUAUHLx
* UQAG_gX-oEBVLOAJDPqak6U_7Pdjm3H460q-2-g5jJqYt8TA
* UQC2fgcn74hlpvCxbVdtZ5gTVSOWHXYHVGXbqC9uB5JBQW_f
* UQCXCdHQu9HQN-fEITMUPVA8IcEB5z0UMkXlNi2mL6hlNBOr
* UQCTd7dmlSgjcjVbWPOcldoeXBgP6NmZcRnpQIWliobe3xk5
* UQAIXBvCyFYdTTXdjgNec5vy-9Tjnqsw_lJ-RFJyA25Mr9M8

### Memepads

Volume includes trades extracted from [TONFun events](https://github.com/re-doubt/ton-etl/blob/main/parser/parsers/message/tonfun.py) for projects: TONPump by HOT Wallet, Blum, BigPump by PocketFi, Wagmi. USD value is calculated as a product of trade amount and price of TON at the time of trade.

### Moki

The same methodology as for RainbowSwap, but with referral address [EQBN9Aw3EauLcUPSjkTV_BmLd-bXaxAuiwak79zjs8g-8Ajg](https://tonviewer.com/EQBN9Aw3EauLcUPSjkTV_BmLd-bXaxAuiwak79zjs8g-8Ajg).

### Titan

The same methodology as for RainbowSwap, but with referral address [EQBPkXS5K-lzRsU6Sz_-qO7UbXU18QVaYrJ1EMmdkBfPaffM](https://tonviewer.com/EQBPkXS5K-lzRsU6Sz_-qO7UbXU18QVaYrJ1EMmdkBfPaffM).


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

TVL originated after tsTON/stTON/STAKED deposits, so it is a sum of all tsTON/stTON/STAKED transfers by the users to 
[the project smart-contract](https://tonviewer.com/EQC2Bt4vwcSgCwABlOfgl75GbGuC0GpRU2GsZKqqMHu-T0gk)

### Aqua Protocol

TVL originated after deposits, so it is a sum of all supported token transfers by the users to 
[the project smart-contract](https://tonviewer.com/EQAWDyxARSl3ol2G1RMLMwepr3v6Ter5ls3jiAlheKshgg0K)

### swap.coffee staking

TVL originated after CES/Ston.fi CES-TON LP/DeDust CES-TON LP deposits, so it is a sum of all transfers CES/Ston.fi CES-TON LP/DeDust CES-TON LP by the users to 
[the project smart-contract](https://tonviewer.com/EQAp-QUzk31pYQWIO5gelCfRrkEe71sI6rg_SvicSV0n31rf)
<br>
And TVL originated after XROCK/Ston.fi XROCK-USDT LP/DeDust XROCK-USDT LP deposits, so it is a sum of all transfers XROCK/Ston.fi XROCK-USDT LP/DeDust XROCK-USDT LP by the users to 
[the project smart-contract](https://tonviewer.com/EQDITerx2VbV-AvnIrva7roz1w0Gis6Xxvwj4b_rVonhyiJW)
<br>
And TVL originated after JETTON/Ston.fi JETTON-USDT LP/DeDust JETTON-USDT LP/Ston.fi JETTON-TON LP/Ston.fi(V2) JETTON-TON LP/DeDust JETTON-TON LP deposits, so it is a sum of all transfers JETTON/Ston.fi JETTON-USDT LP/DeDust JETTON-USDT LP/Ston.fi JETTON-TON LP/Ston.fi(V2) JETTON-TON LP/DeDust JETTON-TON LP by the users to 
[the project smart-contract](https://tonviewer.com/EQAWDTgu0aNz5-hZ0adrMZtKPlyJRfJvyBd2YqxZosZ_OFnj)
<br>
And TVL originated after DFC/Ston.fi DFC-TON LP/DeDust DFC-TON LP deposits, so it is a sum of all transfers DFC/Ston.fi DFC-TON LP/DeDust DFC-TON LP by the users to 
[the project smart-contract](https://tonviewer.com/EQA6yvJtg_m_-LiLckNPtqsjGC9RU-dpCgdVfpYm-IJLq2m3)

### Coffin

Coffin protocol is based on EVAA protocol and uses dedicated router contract EQBozwKVDya9IL3Kw4mR5AQph4yo15EuMdyX8nLljeaUxrpM. Each user can provide liquidity using supply method (and also withdraw it later using withdraw). For each wallet TVL impact is calculated based on amount supplied - amount withdrawn.

### TONCO

TONCO is a CLMM DEX and every time user provides liquidity to the pool, new NFT is minted. 
User can withdraw entire amount of liquidity at any time, when it is done, liquidity goes back to the user
and NFT marked as init=false. So to get all active liqudity positions by the user we are getting all NFTs
from collections owner by [router contract](https://tonviewer.com/EQC_-t0nCnOFMdp7E7qPxAOCbCWGFz-e3pwxb6tTvFmshjt5)
and init=true. Next we are extracting initial liquidity transfers during the NFT mint transaction chain
and estimating that liquidity in USD based on the price of the assets at the time of the transaction.

### Farmix

To count TVL impact for each wallet we are using the following algorightm:

- Getting all JettonPools mints during the season
- Since each mint has preceding deposit transfer, for each jetton mint we are getting jetton transfers within the same trace_id
- Aggregating by wallet address and JettonPool to get two numbers:
    - Total deposit (nominated in the underlying jetton)
    - Total amount minted
- Also getting all burns (i.e. withdrawals) for the JettonPools and adding to the previous table as Total amount burned
- Calculating TVL impact for each wallet using the following formula:
    - (`Total amount minted` - `Total amount burned`) / `Total amount minted`  * `Total deposit` * `Latest price of the asset`

List of Farmix pools:
- [TON](https://tonviewer.com/EQC-jlX83DYZgSWRW5q_XuHLWWFQPp2xGmc8BCoeWckKpeHs)
- [USDT](https://tonviewer.com/EQD6gQSWCayHh0FvUnTXlpfizIWiq7UeE4gYvXGYtEhIYJ8q)
- [NOT](https://tonviewer.com/EQCE_6TevKEpj8OTz3rZt1D5bR6fENQbSN2bbW0jzxbWGGIo)
- [TsTon](https://tonviewer.com/EQC2HxXptnU7vstREZOHyheGTafnFNSlVus5Iwd8Ik89Q7dD)
- [StTon](https://tonviewer.com/EQDuM7dM6mw0vAMurdY0hTNREenlZR1yCurqqo99q3o42nCi)

### Crouton

All users can deposit:
1. [TON/stTON/tsTON](https://crouton.finance/pools/EQB7Orui1z_dKONoHuglvi2bMUpmD4fw0Z4C2gewD2FP0BpL)
2. [DONE/USDT](https://crouton.finance/pools/EQBYyQyeg3n-6REJhKcky4mK5WpmbghRdpAsz-Bi5cJXUWWL)
3. [AquaUSD/USDT](https://crouton.finance/pools/EQB5osFH6kzBN2zK9f3A1LZGeJKmqcyGRumYhJgtuWlbjB8w)

All assets are stored on the following vaults:
- TON – https://tonviewer.com/EQAmCCDmDTi1PAO9ZxH9Mzw7ELKgIjZYoyDPhW07oScrMFhC
- tsTON – https://tonviewer.com/EQDRoyDi8LVQW4CS84GdAuvavSugxoP1LCE49afEpgZMtYIB
- stTON – https://tonviewer.com/EQAdX9rNF0ifkXJAo7CXg5v78yBbP9O1L4UL7M9EI0XMksB0
- USDT – https://tonviewer.com/EQB57BY65_ln-Xv2HpqzstMqoLLVFg_EZPcO0toS-dLlXA2c
- DONE – https://tonviewer.com/EQBmZ_O4suf24Ik8BkkH-dvmkgpNmQfJQWV-iLGjfqltKP2v
- AquaUSD – https://tonviewer.com/EQCM1hd03F1keKNKiB2FBPdT7ebpo0IMIvLMrAmX6bO-IFE9

Users hold LP tokens:
- [TON/stTON/tsTON](https://tonviewer.com/EQB7Orui1z_dKONoHuglvi2bMUpmD4fw0Z4C2gewD2FP0BpL)
- [DONE/USDT](https://tonviewer.com/EQBYyQyeg3n-6REJhKcky4mK5WpmbghRdpAsz-Bi5cJXUWWL)
- [AquaUSD/USDT](https://tonviewer.com/EQB5osFH6kzBN2zK9f3A1LZGeJKmqcyGRumYhJgtuWlbjB8w)

Those are used to estimate TVL increase. Algorithm is the following:

- Calculating increase of Crouton LP balance for each user
- Calculating total supply of Crouton LP at the current moment (or at the end of the season)
- Get actual balances for the vaults at the current moment (or at the end of the season) and estimate total TVL based on the prices of tokens in pools
- User impact is equal to SUM ( `Crouton LP balance increase` / `Total supply of Crouton LP` * `TVL in particular pool` )


### Delea

[Delea](https://app.delea.finance/) is a CDP and users can deposit TON/stTON/tsTON to the pool and mint DONE. Later users 
can repay their position by sending DONE to the vault smart contract (and unlock their underlying collateral).
Vault addresses:
* [TON](https://tonviewer.com/EQB6rkS8xt3Ey4XugdVqQDe1vt4KJDh813_k2ceoONTCBnyD)
* [stTON](https://tonviewer.com/EQA2OzCuP8-d_lN2MYxLv5WCNfpLH1NUuugppOZBZgNYn-aa)
* [tsTON](https://tonviewer.com/EQCwIIRKpuV9fQpQxdTMhLAO30MNHa6GOYd00TsySOOYtA9n)


### CattonFi

Users can provide liquidity into [TON/cTON](https://tonviewer.com/EQAze1aSZHY1yUGz1BFndH62k-VYpXYeDiYofCXTRZClF8Qr) and [USDT/cUSDT](https://tonviewer.com/EQBy7pjr6IBzqW8vuVCZ780evtnkiIF3jZSRRDxeqScfZoU9) pools. The methodology for tracking the user impact to TVL is the same as for Crouton.

Full list of participants and their impact on TVL could be obtained by [this query](sql/s7_defi_tvl.sql).


## Points system

|DeFi Protocol name | Squad | Points per each 20 USD|
|:-|:-|-:|
|Rainbow.ag|Volume|1|
|GasPump|Volume|5|
|swap.coffee|Volume|1|
|TONPump by HOT Wallet|Volume|5|
|Blum|Volume|5|
|BigPump by PocketFi|Volume|5|
|Wagmi|Volume|5|
|Moki|Volume|1|
|Titan|Volume|1|
|Aqua protocol|TVL|10|
|JVault|TVL|5|
|DAOLama|TVL|10|
|Parraton|TVL|10|
|SettleTON|TVL|10|
|TonPools|TVL|5|
|TonStable|TVL|10|
|TON Hedge|TVL|10|
|swap.coffee staking|TVL|5|
|Coffin|TVL|5|
|TONCO|TVL|10|
|Farmix|TVL|10|
|Crouton|TVL|10|
|Delea|TVL|10|
|CattonFi|TVL|10|