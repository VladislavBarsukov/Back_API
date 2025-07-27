import requests
from  Back_API.servises.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    ENDPOINT_PREFIX = "/students"
    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_student(self, json: dict) ->requests.Response:
        response = self.api_utils.post(self.ROOT_ENDPOINT, json=json)
        return response

    def get_student(self, id: int)->requests.Response:
        response = self.api_utils.get(self.ROOT_ENDPOINT+str(id))
        return response

    def put_student(self, id, json:dict)->requests.Response:
        response = self.api_utils.put(self.ROOT_ENDPOINT+str(id), json=json)
        return response

    def delete_student(self, id:int) ->requests.Response:
        response = self.api_utils.delete(self.ROOT_ENDPOINT+str(id))
        return response