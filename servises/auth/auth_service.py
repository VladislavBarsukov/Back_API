from Back_API.servises.auth.helpers.authorization_helper import AuthorizationHelper
from Back_API.servises.auth.helpers.user_helper import UserHelper
from Back_API.servises.auth.model.register_request import RegisterRequest
from Back_API.servises.general.models.success_response import SuccessResponse
from Back_API.utils.api_utils import ApiUtils

from Back_API.servises.auth.model.login_response import LoginResponse
from Back_API.servises.general.base_service import BaseService


class AuthService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.authorization_helper = AuthorizationHelper(self.api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def register_user(self, register_request: RegisterRequest) ->SuccessResponse:
        response = self.authorization_helper.post_register(data=register_request.model_dump())
        return SuccessResponse(**response.json())

    def login_user(self, login_request: RegisterRequest) -> LoginResponse:
        response = self.authorization_helper.post_login(data=login_request.model_dump())
        return LoginResponse(**response.json())
