import requests
from  back_api.servises.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"
    TEMPLATE_ENDPOINT = ROOT_ENDPOINT + "{}"

    def post_student(self, json: dict) ->requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_student(self, id: int)->requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT+str(id))
        return response

    def put_student(self, id, json:dict)->requests.Response:
        response = self.api_utils.put(self.TEMPLATE_ENDPOINT.format(id), json=json)
        return response

    def delete_student(self, id:int) ->requests.Response:
        response = self.api_utils.delete(self.TEMPLATE_ENDPOINT.format(id))
        return response