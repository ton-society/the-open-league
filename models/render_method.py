import glob
import os
from decimal import Decimal

import pandas as pd
import time
from datetime import datetime

from models.results import CalculationResults, ProjectStat
import json
import pathlib
import git

from models.season_config import SeasonConfig

"""
Method to render results
"""
class RenderMethod:
    def __init__(self, icons_base_path):
        self.icons_base_path = icons_base_path

    def render(self, res: CalculationResults, config: SeasonConfig):
        raise NotImplemented()

    def get_commit_hash(self):
        repo = git.Repo(search_parent_directories=True, path=pathlib.Path(__file__).parent.resolve())
        return  repo.head.object.hexsha

    def get_icon(self, project: ProjectStat, config: SeasonConfig):
        # start with detecing icon extension
        prefix = config.leaderboard + "_" + project.name.lower()
        icons = glob.glob(f"{os.path.dirname(os.path.realpath(__file__))}/../projects/icons/{prefix}.*")
        if len(icons) == 0:
            raise Exception(f"No icon found for {project.name}")
        if len(icons) > 1:
            raise Exception(f"Multiple icon formats found for {project.name}")
        format = icons[0].split(".")[-1]
        icon_name = prefix + '.' + format
        if self.icons_base_path:
            return self.icons_base_path + icon_name
        else:
            return icon_name



    def get_items(self, res: CalculationResults, config: SeasonConfig):
        items = []
        for item in res.ranking:
            obj = {
                'name': item.name,
                'score': item.score,
                'icon': self.get_icon(item, config)
            }
            for k, v in item.metrics.items():
                obj[k] = float(v) if type(v) == Decimal else v
            items.append(obj)
        return items


class JsonRenderMethod(RenderMethod):

    def __init__(self, output_name, icons_base_path=None):
        RenderMethod.__init__(self, icons_base_path)
        self.output_name = output_name

    def render(self, res: CalculationResults, config: SeasonConfig):
        items = self.get_items(res, config)
        res = {
            'update_time': res.build_time,
            'build_time': int(time.time()),
            'github_hash': self.get_commit_hash(),
            'source_link': f"https://github.com/ton-society/the-open-league/tree/{self.get_commit_hash()}",
            'items': items
        }
        with open(self.output_name, "wt") as out:
            json.dump(res, out, indent=True)

class HTMLRenderMethod(RenderMethod):
    def __init__(self, output_name, icons_base_path=None):
        RenderMethod.__init__(self, icons_base_path)
        self.output_name = output_name

    def render(self, res: CalculationResults, config: SeasonConfig):
        items = self.get_items(res, config)
        table = pd.DataFrame(items).to_html()
        with open(self.output_name, "wt") as out:
            out.write(f"<html><head>Results for {config.name}</head><body>")
            out.write(f"<h2>Results for {config.leaderboard} leaderboard {config.name}</h2>")
            out.write(f"<h2>Data update time: "
                      f"{datetime.utcfromtimestamp(res.build_time).strftime('%Y-%m-%d %H:%M:%S')}</h2>")
            out.write(table)
            out.write("</body></html>")