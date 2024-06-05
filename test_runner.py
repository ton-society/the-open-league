"""
Test runner for github tests
"""
import sys

from loguru import logger

from backends.tonalytica.apps import TonalyticaAppBackend
from backends.tonalytica.tokens import TonalyticaTokensBackend
from seasons.s3_5 import S3_5_apps, S3_5_tokens

if __name__ == "__main__":
    backend = TonalyticaTokensBackend()
    season = S3_5_tokens
    res = backend.calculate(season, dry_run=len(sys.argv) > 1 and sys.argv[1] == '--dryrun')
    logger.info(res)