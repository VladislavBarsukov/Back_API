from faker import Faker
import random
from Back_API.logger.logger import Logger
from Back_API.servises.university.models.group_request import GroupRequest
from Back_API.servises.university.models.student_request import StudentRequest
from Back_API.servises.university.university_service import UniversityService

faker = Faker()


class TestStudentCreate:

    def test_student_create(self, university_api_utils_admin):
        Logger.info("Create group, step 1")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)

        Logger.info("Create student with created group, step 2")
        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice(["Bachelor", "Associate", "Master",
                                                       "Doctorate"]),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group_response.id)
        student_response = university_service.create_student(student_request=student)
        assert student_response.group_id == group_response.id, f"Wrong group, expected {group_response.id}, get {student_response.group_id}"

        Logger.info("Get created student, step 3")
        get_student_by_id = university_service.get_student(student_id=student_response.id)
        assert get_student_by_id.id == student_response.id, f"Wrong id, expected {get_student_by_id.id}, get {student_response.id}"