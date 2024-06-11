from decimal import Decimal

import pandas as pd
import time
from datetime import datetime

from models.results import CalculationResults
import json
import git

from models.season_config import SeasonConfig

"""
Method to render results
"""
class RenderMethod:
    def render(self, res: CalculationResults, config: SeasonConfig):
        raise NotImplemented()

    def get_commit_hash(self):
        repo = git.Repo(search_parent_directories=True)
        return  repo.head.object.hexsha

    def get_items(self, res: CalculationResults):
        items = []
        for item in res.ranking:
            obj = {
                'name': item.name,
                'score': item.score
            }
            for k, v in item.metrics.items():
                obj[k] = float(v) if type(v) == Decimal else v
            items.append(obj)
        return items


class JsonRenderMethod(RenderMethod):
    def __init__(self, output_name):
        self.output_name = output_name

    def render(self, res: CalculationResults, config: SeasonConfig):
        items = self.get_items(res)
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
    def __init__(self, output_name):
        self.output_name = output_name

    def render(self, res: CalculationResults, config: SeasonConfig):
        items = self.get_items(res)
        table = pd.DataFrame(items).to_html()
        with open(self.output_name, "wt") as out:
            out.write(f"<html><head>Results for {config.name}</head><body>")
            out.write(f"<h2>Results for {config.leaderboard} leaderboard {config.name}</h2>")
            out.write(f"<h2>Data update time: "
                      f"{datetime.utcfromtimestamp(res.build_time).strftime('%Y-%m-%d %H:%M:%S')}</h2>")
            out.write(table)
            out.write("</body></html>")