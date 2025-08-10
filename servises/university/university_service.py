from back_api.servises.general.base_service import BaseService
from back_api.servises.university.helpers.group_helper import GroupHelper
from back_api.servises.university.helpers.student_helper import StudentHelper
from back_api.servises.university.models.group_request import GroupRequest
from back_api.servises.university.models.group_response import GroupResponse
from back_api.servises.university.models.student_request import StudentRequest
from back_api.servises.university.models.student_response import StudentResponse
from back_api.utils.api_utils import ApiUtils


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(
            json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(
            self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(
            json=student_request.model_dump())
        return StudentResponse(**response.json())

    def update_student(self, student_id,
                       student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.put_student(
            student_id, json=student_request.model_dump())
        return StudentResponse(**response.json())

    def get_student(self, student_id) -> StudentResponse:
        response = self.student_helper.get_student(student_id)
        return StudentResponse(**response.json())

    def delete_student(self, student_id) -> dict:
        response = self.student_helper.delete_student(student_id)
        return response.json()
