"""
Test runner for github tests
"""
import sys

from loguru import logger

from backends.redoubt.apps import RedoubtAppBackend
from backends.redoubt.tokens import RedoubtTokensBackend
from models.render_method import JsonRenderMethod, HTMLRenderMethod
from seasons.s3_5 import S3_5_apps, S3_5_tokens, S3_5_tokens_old

if __name__ == "__main__":
    backend = RedoubtTokensBackend()
    season = S3_5_tokens
    res = backend.calculate(season, dry_run=len(sys.argv) > 1 and sys.argv[1] == '--dryrun')
    logger.info(res)
    render = JsonRenderMethod("output_s3_5.json")
    render.render(res, season)
    render = HTMLRenderMethod("output_s3_5.html")
    render.render(res, season)
