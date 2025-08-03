from enum import StrEnum
from back_api.servises.university.utils.student_data_generator import StudentDataGenerator
from faker import Faker
import random
from back_api.logger.logger import Logger
from back_api.servises.university.models.group_request import GroupRequest
from back_api.servises.university.models.student_request import StudentRequest
from back_api.servises.university.university_service import UniversityService
from back_api.servises.university.utils.steps import Steps

faker = Faker()


class TestStudentUpdate:

    def test_update_created_student(self, university_api_utils_admin):
        Logger.info("Starting test: test_update_created_student")
        university_service = UniversityService(api_utils=university_api_utils_admin)
        test_steps = Steps(university_service)

        Logger.info("Create group, step 1")
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)

        Logger.info("Create student, step 2")
        student_create_response = test_steps.create_student(group_id=group_response)

        Logger.info("Update created student, step 3")
        group = GroupRequest(name=faker.name())
        group_response = university_service.create_group(group_request=group)
        student_update = StudentDataGenerator.generate_student_data(group_id=group_response)
        student_update_response = university_service.update_student(student_id=student_create_response.id,
                                                                    student_request=student_update)
        Logger.info("Get updated student, step 4")
        get_updated_student_by_id = university_service.get_student(student_id=student_update_response.id)
        assert student_create_response != get_updated_student_by_id, "Student wasn't updated"
