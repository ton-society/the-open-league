"""
Test runner for github tests
"""
from backends.tonalytica import TonalyticaAppBackend
from loguru import logger
from seasons.s3_5 import S3_5_apps

if __name__ == "__main__":
    backend = TonalyticaAppBackend()
    season = S3_5_apps
    res = backend.calculate(season, dry_run=False)
    logger.info(res)