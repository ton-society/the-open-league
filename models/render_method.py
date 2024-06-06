from models.results import CalculationResults
import json


"""
Method to render results
"""
class RenderMethod:
    def render(self, res: CalculationResults):
        raise NotImplemented()


class JsonRenderMethod(RenderMethod):
    def __init__(self, output_name):
        self.output_name = output_name

    def render(self, res: CalculationResults):
        items = []
        for item in res.ranking:
            obj = {
                'name': item.name,
                'score': item.score
            }
            for k, v in item.metrics.items():
                obj[k] = v
            items.append(obj)
        res = {
            'build_time': res.build_time,
            'items': items
        }
        with open(self.output_name, "wt") as out:
            json.dump(res, out)
