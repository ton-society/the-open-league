import requests

"""
Wrapper to call contract-executor - https://github.com/shuva10v/contracts-executor
"""
class ContractsExecutor:
    def __init__(self, api_url):
        self.api_url = api_url

    def execute(self, code, data, address, method, types):
        request = {'code': code, 'data': data, 'method': method,
               'expected': types, 'address': address, 'arguments': []}
        res = requests.post(self.api_url, json=request)
        return res.json()['result']