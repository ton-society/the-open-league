# The Open League

This repository contains code for The Open League metrics calculation.

## Architecture

The Open League consists of multiple leaderboards showcasing project rankings. 
These rankings are based on specific metrics and are calculated for a particular season, 
a set period of time with a defined list of projects and rules.

The primary objective of this repository is to establish a Domain Specific Language (DSL) 
for leaderboards, projects, and seasons. Using this DSL, all ranks can be calculated 
through backends. A backend is an implementation of metrics calculation based on a 
specific data source. Currently, there are two backends:
* re:doubt DB, which is based on [ton-indexer](https://github.com/re-doubt/ton-indexer) and 
[Tonalytica](https://tonalytica.redoubt.online/). It is used for all leaderboards except of DeFi.
* [DefiLlama](./backends/defi.py) with on-chain data from [Tonapi](https://tonapi.io/) - used for the DeFi Leaderboard.

Main entities:
* [Metric](./models/metrics/) - used for the App Leaderboard, a simple way to describe
on-chain mechanics for applications. Each metric must contains backend-specific implementation.
(see [an example](./models/metrics/smc_interaction.py))
* [Backend](./backends) - metrics calculation backend per leaderboard. 
* [ProjectStats](./models/results.py) - results of calculation, contains key-value dict with metrics values
* [Project](./projects) - all information about particular project. For applications
must contain all possible interactions and unique off-chain analytics tag.
* [SeasonConfig](./models/season_config.py) - season config: time period, list of projects,
scoring formula, etc..
* [ScoreModel](./models/scores.py) - final formula to get scores for each project based on metrics

## Season

List of the seasons supported with the leaderboard links

| Season                                                                              | Results                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 
|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [S3.5](./seasons/s3_5.py) - test season (no actual competition), between S3 and S4. | <ul><li>Tokens: [HTML](https://the-open-league-static-data.s3.amazonaws.com/season/s3_5/token.html), [JSON](https://the-open-league-static-data.s3.amazonaws.com/season/s3_5/token.json)</li><li>Apps: [HTML](https://the-open-league-static-data.s3.amazonaws.com/season/s3_5/app.html), [JSON](https://the-open-league-static-data.s3.amazonaws.com/season/s3_5/app.json)</ul>                                                                                                                                                                                   |
| [S4](./seasons/s4.py) - [Methodology](https://ton-org.notion.site/TOL-Season-4-Methodology-30e741e37eb64933b1cd5e61c4546033)                                             | <ul><li>Tokens: [HTML](https://the-open-league-static-data.s3.amazonaws.com/season/S4/tokens.html), [JSON](https://the-open-league-static-data.s3.amazonaws.com/season/S4/tokens.json)</li><li>Apps: [HTML](https://the-open-league-static-data.s3.amazonaws.com/season/S4/apps.html), [JSON](https://the-open-league-static-data.s3.amazonaws.com/season/S4/apps.json)</li><li>DeFi: [HTML](https://the-open-league-static-data.s3.amazonaws.com/season/S4/defi.html), [JSON](https://the-open-league-static-data.s3.amazonaws.com/season/S4/defi.json)</li></ul> |

## Adding metrics for your project

To add new project one need to create a file in [projects/{type}/{slug.py}](./projects) folder,
where type is __apps__ or __token__ and __slug__ is project name.

To add more contracts please find your project file in [projects](./projects) folder
and add metrics you need. The full list of supported metrics is [here](./models/metrics).
 
## Running configuration

To run metrics calculation one needs to use existing [SeasonConfig](./seasons) and configured backend.
In general backends require some params and resources preconfigured (like DB connection).
Simple example of running different backends is provided in [test_runnger.py](./test_runner.py).

### Re:doubt backend

One need to pass postgres db connection. Below is an example for running via Apache Airflow:
```python
postgres_hook = PostgresHook(postgres_conn_id="db")
backend = RedoubtAppBackend(postgres_hook.get_conn())
results = backend.calculate(S4_app)
OUTPUT_JSON = "output.json"
OUTPUT_HTML = "output.html"
render = JsonRenderMethod(OUTPUT_JSON)
render.render(results, season_config)
render = HTMLRenderMethod(OUTPUT_HTML)
render.render(results, season_config)
```

### DeFiLlama backend

It requires data from DeFiLlama (public, doesn't require auth) and 
tonapi (API key is recommended). Also, [contract-executor](https://github.com/shuva10v/contracts-executor) tool
is required. Example of running config:
```python
backend  = DefillamaDeFiBackend(
                tonapi=TonapiAdapter("ABCD...."),
                executor=ContractsExecutor("http://localhost:9090/execute")
            )
results = backend.calculate(S4_defi)
...
```