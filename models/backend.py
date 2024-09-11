
"""
Main class for all calculation backends
"""
from models.results import CalculationResults
from models.season_config import SeasonConfig
from loguru import logger


class CalculationBackend:
    def __init__(self, name, leaderboards=[]):
        self.name = name
        self.leaderboards = leaderboards # list of supported leaderboards

    def calculate(self, config: SeasonConfig, dry_run: bool = False):
        if not dry_run:
            update_time = int(self.get_update_time(config))
        if config.leaderboard not in self.leaderboards:
            raise Exception(f"Leaderboard {config.leaderboard} is not supported")
        res = self._do_calculate(config, dry_run)
        if isinstance(res, CalculationResults):
            logger.info(f"Applying scoring model to {res}")
            res.ranking = config.score_model.calculate(res.ranking)
        if not dry_run and res:
            res.build_time = update_time
        return res

    """
    Update time may be different from the current time, so
    each backend should provide exact value here. 
    Possible solution is to provide last block time at the moment of invocation
    """
    def get_update_time(self, config: SeasonConfig):
        raise NotImplemented()

    def _do_calculate(self, config: SeasonConfig, dry_run: bool = False):
        raise NotImplemented()
