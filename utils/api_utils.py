import json

import curlify
from requests import Session

from back_api.utils.json_utils import JsonUtils
from back_api.logger.logger import Logger


def log_response(func):
    def _log_response(*args, **kwargs):
        response = func(*args, **kwargs)
        Logger.info(f"Request: {curlify.to_curl(response.request)}")
        body = json.dumps(response.json(), indent=2) if JsonUtils.is_json(response.text) else response.text
        Logger.info(f"Response status code: '{response.status_code}', elapsed_time='{response.elapsed}'\n{body}\n")
        return response
    return _log_response


class ApiUtils:
    def __init__(self, url, headers=None):
        if headers is None:
            headers = {}
        self.session = Session()
        self.session.headers.update(headers)
        self.url = url

    @log_response
    def get(self, endpoint_url, **kwargs):
        response = self.session.get(self.url + endpoint_url, **kwargs)
        return response

    @log_response
    def put(self, endpoint_url, **kwargs):
        response = self.session.put(self.url + endpoint_url, **kwargs)
        return response

    @log_response
    def post(self, endpoint_url, data=None, json=None, **kwargs):
        response = self.session.post(self.url + endpoint_url, data, json, **kwargs)
        return response

    @log_response
    def delete(self, endpoint_url, **kwargs):
        response= self.session.delete(self.url + endpoint_url, **kwargs)
        return response