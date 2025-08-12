from faker import Faker

from back_api.servises.university.models.group_request import GroupRequest
from back_api.servises.university.utils.student_data_generator import \
    StudentDataGenerator

faker = Faker()


class Steps:
    def __init__(self, university_service):
        self.university_service = university_service

    def create_group(self):
        group = GroupRequest(name=faker.name())
        response = self.university_service.create_group(group_request=group)
        return response

    def create_student(self, group_id):
        student_data = StudentDataGenerator.generate_student_data(group_id=group_id)
        response = self.university_service.create_student(student_request=student_data)
        return response
