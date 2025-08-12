import random
from enum import StrEnum

from faker import Faker

from back_api.servises.university.models.student_request import StudentRequest

faker = Faker()


class Degree(StrEnum):
    BACHELOR = "Bachelor"
    ASSOCIATE = "Associate"
    MASTER = "Master"
    DOCTORATE = "Doctorate"


class StudentDataGenerator:
    @staticmethod
    def generate_student_data(group_id=None):
        return StudentRequest(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            degree=random.choice(
                [Degree.BACHELOR, Degree.ASSOCIATE, Degree.MASTER, Degree.DOCTORATE]
            ),
            phone=faker.numerify("+7##########"),
            group_id=group_id.id,
        )
