from Back_API.servises.auth.helpers.authorization_helper import AuthorizationHelper
from Back_API.servises.auth.helpers.user_helper import UserHelper
from Back_API.servises.auth.model.register_request import RegisterRequest
from Back_API.servises.general.models.success_response import SuccessResponse
from Back_API.utils.api_utils import ApiUtils
from Back_API.servises.general.base_service import BaseService
from Back_API.servises.university.helpers.group_helper import GroupHelper
from Back_API.servises.university.helpers.student_helper import StudentHelper
from Back_API.servises.university.models.group_request import GroupRequest
from Back_API.servises.university.models.group_response import GroupResponse
from Back_API.servises.university.models.student_request import StudentRequest
from Back_API.servises.university.models.student_response import StudentResponse
from requests import HTTPError, Response

class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.group_helper = GroupHelper(self.api_utils)
        self.student_helper = StudentHelper(self.api_utils)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        response = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**response.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        response = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**response.json())

    def update_student(self, student_id, student_request: StudentRequest)-> StudentResponse:
        response = self.student_helper.put_student(student_id, json=student_request.model_dump())
        return StudentResponse(**response.json())

    def get_student(self, student_id) -> StudentResponse | str:
        try:
            response = self.student_helper.get_student(student_id)
            response.raise_for_status()
            return StudentResponse(**response.json())
        except HTTPError as e:
            if e.response.status_code == 404:
                return "Not found"
            else:
                raise

    def delete_student(self, student_id) -> str:
        response: Response = self.student_helper.delete_student(student_id)
        try:
            response.raise_for_status()
            return "Student deleted"
        except HTTPError as e:
            if e.response.status_code == 404:
                return "Not found"
            else:
                raise
