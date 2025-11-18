from faker import Faker

from back_api.logger.logger import Logger
from back_api.servises.university.models.group_request import GroupRequest
from back_api.servises.university.university_service import UniversityService
from back_api.servises.university.utils.steps import Steps

faker = Faker()


class TestStudentCreate:
    def test_student_create(self, university_api_utils_admin):
        Logger.info("Starting test: test_creat_student")
        university_service = UniversityService(
            api_utils=university_api_utils_admin)
        test_steps = Steps(university_service)

        Logger.info("Create group, step 1")
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)

        Logger.info("Create student, step 2")
        student_response = test_steps.create_student(group_id=group_response)

        Logger.info("Assert student id, step 3")
        get_student_by_id = university_service.get_student(
            student_id=student_response.id
        )
        assert get_student_by_id.id == student_response.id, f"Wrong id, expected {get_student_by_id.id}, get {student_response.id}"
