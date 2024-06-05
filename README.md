# The Open League

This repository contains code for The Open League metrics calculation.

## Architecture

The Open League contains multiple leaderboard with the project ranking.
Ranking is based on metrics and computed for a particular Season - period of
time with a fixed project's list and rules.

The main goal of this repo is to create DSL for leaderboards, projects 
and seasons. Based on this DSL all ranks could be calculated
using backends. Backend is an implementation of metrics calculation
based on specific data source. For now the only supported backend
is [Tonalytica](https://tonalytica.redoubt.online/).

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

List of the seasons supported:
* [S3.5](./seasons/s3_5.py) - test season (no actual competition), between S3 and S4.

## Documentation

Auto-generated documentation for the app leaderboard will be added soon

## Adding metrics for your project

To add new project one need to create a file in [projects/{type}/{slug.py}](./projects) folder,
where type is __apps__ or __token__ and __slug__ is project name.
