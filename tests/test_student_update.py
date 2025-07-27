from faker import Faker
import random
from Back_API.logger.logger import Logger
from Back_API.servises.university.models.group_request import GroupRequest
from Back_API.servises.university.models.student_request import StudentRequest
from Back_API.servises.university.university_service import UniversityService

faker = Faker()


class TestStudentUpdate:

    def test_update_created_student(self, university_api_utils_admin):
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
        student_create_response = university_service.create_student(student_request=student)

        Logger.info("Update created student, step 3")
        student_update = StudentRequest(first_name=faker.first_name(),
                                        last_name=faker.last_name(),
                                        email=faker.email(),
                                        degree=random.choice(["Bachelor", "Associate", "Master",
                                                              "Doctorate"]),
                                        phone=faker.numerify("+7##########"),
                                        group_id=group_response.id)
        student_update_response = university_service.update_student(student_id=student_create_response.id,
                                                                    student_request=student_update)
        Logger.info("Get updated student, step 4")
        get_updated_student_by_id = university_service.get_student(student_id=student_update_response.id)
        assert student_create_response != get_updated_student_by_id, "Student wasn't updated"