import requests.status_codes
from faker import Faker

from back_api.servises.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestCreateGroupContract:
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": faker.name()})
        assert (
            response.status_code == requests.status_codes.codes.unauthorized
        ), f"Wrong status code, Actual: '{response.status_code}', expected {requests.status_codes.codes.unauthorized}"

    def test_create_group_admin(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.post_group({"name": faker.name()})
        assert (
            response.status_code == requests.status_codes.codes.created
        ), f"Wrong status code, Actual: '{response.status_code}', expected {requests.status_codes.codes.unauthorized}"

    def test_create_same_group_admin(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.post_group({"name": faker.name()})
        same_name = response.json()["name"]
        response = group_helper.post_group({"name": same_name})
        assert (
            response.status_code == requests.status_codes.codes.conflict
        ), f"Wrong status code, Actual: '{response.status_code}', expected {requests.status_codes.codes.unauthorized}"

    def test_create_group_admin_no_name(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.post_group({"name": None})
        assert (
            response.status_code == requests.status_codes.codes.unprocessable_content
        ), f"Wrong status code, Actual: '{response.status_code}', expected {requests.status_codes.codes.unauthorized}"
