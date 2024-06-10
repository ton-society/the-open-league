import time

from models.season_config import SeasonConfig
from s3_5 import S3_5_apps
import time

from seasons.app_models import AppLeaderboardModelV2

start_time = int(time.time()) - 3 * 3600 # 3 hours to mitigate possible indexer lag
LAST_30DAYS_MAU_SEASON = SeasonConfig(
    leaderboard=SeasonConfig.APPS,
    name="last",
    start_time=start_time - 30 * 86400,
    end_time=start_time,
    projects=S3_5_apps.projects,
    score_model=AppLeaderboardModelV2()
)