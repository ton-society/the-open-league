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

## Adding metrics for your project

To add new project one need to create a file in [projects/{type}](./projects) folder,
where type is __apps__ or __token__.

TODO - add examples