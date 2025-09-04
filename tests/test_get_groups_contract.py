import requests.status_codes
from faker import Faker

from back_api.servises.university.helpers.group_helper import GroupHelper

faker = Faker()


class TestGetGroupContract:
    def test_get_groups_admin(self, university_api_utils_admin):
        group_helper = GroupHelper(api_utils=university_api_utils_admin)
        response = group_helper.get_groups()
        assert (
            response.status_code == requests.status_codes.codes.okay
        ), f"Wrong status code, Actual: '{response.status_code}', expected '{requests.status_codes.codes.okay}'"

    def test_get_groups_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.get_groups()
        assert (
            response.status_code == requests.status_codes.codes.unauthorized
        ), f"Wrong status code, Actual: '{response.status_code}', expected {requests.status_codes.codes.unauthorized}"
