import time
import pytest
from back_api.utils.api_utils import ApiUtils
from back_api.servises.auth.auth_service import AuthService
from faker import Faker
from back_api.servises.auth.model.login_request import LoginRequest
from back_api.servises.auth.model.register_request import RegisterRequest
from back_api.servises.university.university_service import UniversityService
import requests

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_utils_anonym):
    auth_service = AuthService(auth_api_utils_anonym)
    username = faker.user_name()
    password = faker.password(length=30,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    auth_service.register_user(register_request=RegisterRequest(username=username,
                                                                password=password,
                                                                password_repeat=password,
                                                                email=faker.email()))
    login_response = auth_service.login_user(
        login_request=LoginRequest(
            username=username, password=password))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_api_utils_admin(access_token):
    api_utils = ApiUtils(
        url=AuthService.SERVICE_URL, headers={
            "Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_utils_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL, headers={
                         "Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope='session', autouse=True)
def auth_service_readiness():
    timeout = 100
    start_time = time.time()
    while time.time() < start_time + timeout:
        try:
            response = requests.get(AuthService.SERVICE_URL + "/docs")
            response.raise_for_status()
        except BaseException:
            time.sleep(1)
        else:
            break
    else:
        raise RuntimeError(
            f"Auth service wasn't started during {timeout} seconds.")
