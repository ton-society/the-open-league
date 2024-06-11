"""
Test runner for github tests
"""
import sys

import psycopg2
from loguru import logger

from backends.redoubt.apps import RedoubtAppBackend
from backends.redoubt.nfts import RedoubtNFTsBackend
from backends.redoubt.tokens import RedoubtTokensBackend
from models.render_method import JsonRenderMethod, HTMLRenderMethod
from seasons.s3_5 import S3_5_apps, S3_5_tokens, S3_5_nfts

if __name__ == "__main__":
    with psycopg2.connect() as conn:
        if sys.argv[1] == 'tokens':
            backend = RedoubtTokensBackend(conn)
            season = S3_5_tokens
        elif sys.argv[1] == 'apps':
            backend = RedoubtAppBackend(conn)
            season = S3_5_apps
        elif sys.argv[1] == 'nfts':
            backend = RedoubtNFTsBackend(conn)
            season = S3_5_nfts
        else:
            raise Exception(f"leadeboard not supported: {sys.argv[1]}")

        res = backend.calculate(season, dry_run=len(sys.argv) > 2 and sys.argv[2] == '--dryrun')
        logger.info(res)
        render = JsonRenderMethod("output_s3_5.json")
        render.render(res, season)
        render = HTMLRenderMethod("output_s3_5.html")
        render.render(res, season)
