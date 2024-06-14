#!/usr/bin/env python

import glob
import importlib.util
import sys

from models.icons import get_icon_name
from models.season_config import SeasonConfig

if __name__ == '__main__':
    for file in glob.glob("seasons/s*py"):
        # some weird Python introspection hacks to ge all seasons and extract all projects
        season_name = file.split("/")[1].split(".")[0]
        import_stmt = f"seasons.{season_name}"
        print(f"Importing {import_stmt}")
        m = __import__(import_stmt)
        for name, season_config in dict([(name, cls) for name, cls in m.__dict__.items() if isinstance(cls, SeasonConfig)]).items():
            print(f"Checking {name} from {season_name}")
            for project in season_config.projects:
                get_icon_name(season_config, project)
