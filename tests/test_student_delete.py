import requests.status_codes
from faker import Faker

from back_api.logger.logger import Logger
from back_api.servises.university.helpers.student_helper import StudentHelper
from back_api.servises.university.models.group_request import GroupRequest
from back_api.servises.university.university_service import UniversityService
from back_api.servises.university.utils.steps import Steps

faker = Faker()


class TestStudentDelete:
    def test_student_delete(self, university_api_utils_admin):
        Logger.info("Starting test: test_delete_student")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        test_steps = Steps(university_service)
        Logger.info("Create group, step 1")
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)
        Logger.info("Create student, step 2")
        student_response = test_steps.create_student(group_id=group_response)
        Logger.info("Delete student, step 3")
        university_service.delete_student(student_response.id)
        Logger.info("Get deleted student, step 4")
        helper = StudentHelper(university_api_utils_admin)
        response = helper.get_student(student_response.id)
        assert (
            response.status_code == requests.status_codes.codes.not_found
        ), f"Expected {requests.status_codes.codes.not_found}, get {
            response.status_code
        }"
