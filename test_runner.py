"""
Test runner for github tests
"""
import os
import sys

import psycopg2
from loguru import logger

from backends.contracts_executor import ContractsExecutor
from backends.defillama.tvl import DefillamaDeFiTVLBackend
from backends.defillama.volume import DefillamaDeFiVolumeBackend
from backends.sbt_enrollment import SBTEnrollmentSync
from backends.redoubt.apps import RedoubtAppBackend
from backends.redoubt.apps_v2 import RedoubtAppBackendV2
from backends.toncenter_cpp.apps_v2_users import ToncenterCppAppBackendV2Users
from backends.toncenter_cpp.nfts import ToncenterCppNFTsBackend
from backends.redoubt.tokens import RedoubtTokensBackend
from backends.tonapi import TonapiAdapter
from backends.toncenter_cpp.apps_v2_projects import ToncenterCppAppsScores2Projects
from models.render_method import JsonRenderMethod, HTMLRenderMethod
from models.season_config import SeasonConfig
from seasons.s6 import S6_apps, S6_nfts
from seasons.s7 import S7_defi_volume, S7_defi_tvl

if __name__ == "__main__":
    with psycopg2.connect() as conn:
        if sys.argv[1] == 'apps_v2':
            backend = ToncenterCppAppBackendV2Users(conn, produce_output=True)
            season = S6_apps
            backend.calculate(season, dry_run=len(sys.argv) > 2 and sys.argv[2] == '--dryrun')
        elif sys.argv[1] == 'apps_v2_projects':
            backend = ToncenterCppAppsScores2Projects(conn)
            season = S6_apps
            backend.calculate(season, dry_run=len(sys.argv) > 2 and sys.argv[2] == '--dryrun')
        elif sys.argv[1] == 'nfts':
            backend = ToncenterCppNFTsBackend(conn)
            season = S6_nfts
        elif sys.argv[1] == 'defi_tvl':
            backend = DefillamaDeFiTVLBackend(
                tonapi=TonapiAdapter(),
                executor=ContractsExecutor(os.getenv('CONTRACTS_EXECUTOR_URL'))
            )
            season = S7_defi_tvl
        elif sys.argv[1] == 'defi_volume':
            backend = DefillamaDeFiVolumeBackend()
            season = S7_defi_volume
        elif sys.argv[1] == 'sbt':
            backend = SBTEnrollmentSync(conn,
                tonapi=TonapiAdapter(),
                executor=ContractsExecutor(os.getenv('CONTRACTS_EXECUTOR_URL')))
            season = S6_apps
            backend.sync(season)
            sys.exit(0)
        else:
            raise Exception(f"leaderboard not supported: {sys.argv[1]}")

        res = backend.calculate(season, dry_run=len(sys.argv) > 2 and sys.argv[2] == '--dryrun')
        logger.info(res)
        render = JsonRenderMethod("output.json")
        render.render(res, season)
        render = HTMLRenderMethod("output.html")
        render.render(res, season)
