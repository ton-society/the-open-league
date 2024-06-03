
"""
Main class for all calculation backends
"""
from models.season_config import SeasonConfig


class CalculationBackend:
    def __init__(self, name, leaderboards=[]):
        self.name = name
        self.leaderboards = leaderboards # list of supported leaderboards

    def calculate(self, config: SeasonConfig, dry_run: bool = False):
        if config.leaderboard not in self.leaderboards:
            raise Exception(f"Leaderboard {config.leaderboard} is not supported")
        return self._do_calculate(config, dry_run)

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        raise NotImplemented()
