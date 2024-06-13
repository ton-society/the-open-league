import base64
import os
import requests
from urllib.parse import quote_plus
from tonsdk.boc import Cell


"""
Tonapi calls implementation
"""
class TonapiAdapter:
    def __init__(self, api_key=None):
        self.api_key = api_key
        if self.api_key is None:
            self.api_key = os.getenv('TONAPI_API_KEY', None)
        if self.api_key:
            self.auth_header = {
                'Authorization': 'Bearer %s' % self.api_key
            }
        else:
            self.auth_header = {}

    def get_state(self, address, target_block):
        res = requests.get(f'https://tonapi.io/v2/liteserver/get_account_state/{quote_plus(address)}' +
                           (f'?target_block={quote_plus("(" + target_block + ")")}' if target_block else ''),
                           headers=self.auth_header).json()
        state = Cell.one_from_boc(res['state']).begin_parse()
    
        def to_b64(cell):
            return base64.b64encode(cell.to_boc()).decode('utf-8')
        code = to_b64(state.refs[0])
        data = to_b64(state.refs[1])
        return code, data