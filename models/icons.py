import glob
import os

from models.season_config import SeasonConfig


def get_icon_name(config: SeasonConfig, project: any):
    # start with detecing icon extension
    prefix = config.leaderboard + "_" + project.name.lower()
    icons = glob.glob(f"{os.path.dirname(os.path.realpath(__file__))}/../projects/icons/{prefix}.*")
    if len(icons) == 0:
        raise Exception(f"No icon found for {project.name}")
    if len(icons) > 1:
        raise Exception(f"Multiple icon formats found for {project.name}")
    format = icons[0].split(".")[-1]
    return prefix + '.' + format