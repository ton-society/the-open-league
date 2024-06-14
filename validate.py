#!/usr/bin/env python

import glob
from PIL import Image

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
                image = get_icon_name(season_config, project)
                if image.endswith(".svg"):
                    continue
                assert image.endswith(".png"), "Only png and svg formats are supported"
                image_obj = Image.open("projects/icons/" + image)
                assert image_obj.size == (100, 100), f"Image {image} for project {project.name} " \
                                                     f"has wrong dimensions: %dx%d" % image_obj.size
                
