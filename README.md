# The Open League

This repository contains code for The Open League metrics calculation.

## Architecture

The Open League consists of multiple leaderboards showcasing project rankings. 
These rankings are based on specific metrics and are calculated for a particular season, 
a set period of time with a defined list of projects and rules.

The primary objective of this repository is to establish a Domain Specific Language (DSL) 
for leaderboards, projects, and seasons. Using this DSL, all ranks can be calculated 
through backends. A backend is an implementation of metrics calculation based on a 
specific data source. Currently, the only supported backend is re:doubt DB, 
which is based on [ton-indexer](https://github.com/re-doubt/ton-indexer) and 
[Tonalytica](https://tonalytica.redoubt.online/).

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

| Season | Results                                                                                                                                                                                                                                                                                                                                                                            | Runner                                 |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
|  [S3.5](./seasons/s3_5.py) - test season (no actual competition), between S3 and S4.      | <ul><li>Tokens: [HTML](https://the-open-league-static-data.s3.amazonaws.com/season/s3_5/token.html), [JSON](https://the-open-league-static-data.s3.amazonaws.com/season/s3_5/token.json)</li><li>Tokens: [HTML](https://the-open-league-static-data.s3.amazonaws.com/season/s3_5/app.html), [JSON](https://the-open-league-static-data.s3.amazonaws.com/season/s3_5/app.json)</ul> | [season3_5.py](./runners/season3_5.py) |

## Adding metrics for your project

To add new project one need to create a file in [projects/{type}/{slug.py}](./projects) folder,
where type is __apps__ or __token__ and __slug__ is project name.
 
