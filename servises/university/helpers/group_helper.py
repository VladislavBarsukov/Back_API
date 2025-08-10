
import requests

from back_api.servises.general.helpers.base_helper import BaseHelper


class GroupHelper(BaseHelper):
    ENDPOINT_PREFIX = "/groups"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_group(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_groups(self):
        response = self.api_utils.get(self.ROOT_ENDPOINT)
        return response
