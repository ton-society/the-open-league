"""
Test runner for github tests
"""
import os
import sys

import psycopg2
from loguru import logger

from backends.contracts_executor import ContractsExecutor
from backends.defi import DefillamaDeFiBackend
from backends.redoubt.apps import RedoubtAppBackend
from backends.redoubt.nfts import RedoubtNFTsBackend
from backends.redoubt.tokens import RedoubtTokensBackend
from backends.tonapi import TonapiAdapter
from models.render_method import JsonRenderMethod, HTMLRenderMethod
from models.season_config import SeasonConfig
from seasons.s4 import S4_apps, S4_tokens, S4_nfts, S4_defi

if __name__ == "__main__":
    with psycopg2.connect() as conn:
        if sys.argv[1] == 'tokens':
            backend = RedoubtTokensBackend(conn)
            season = S4_tokens
        elif sys.argv[1] == 'apps':
            backend = RedoubtAppBackend(conn)
            season = S4_apps
        elif sys.argv[1] == 'nfts':
            backend = RedoubtNFTsBackend(conn)
            season = S4_nfts
        elif sys.argv[1] == 'defi':
            backend = DefillamaDeFiBackend(
                tonapi=TonapiAdapter(),
                executor=ContractsExecutor(os.getenv('CONTRACTS_EXECUTOR_URL'))
            )
            season = S4_defi
        else:
            raise Exception(f"leaderboard not supported: {sys.argv[1]}")

        res = backend.calculate(season, dry_run=len(sys.argv) > 2 and sys.argv[2] == '--dryrun')
        logger.info(res)
        render = JsonRenderMethod("output.json")
        render.render(res, season)
        render = HTMLRenderMethod("output.html")
        render.render(res, season)
