from back_api.servises.auth.helpers.authorization_helper import AuthorizationHelper
from back_api.servises.auth.helpers.user_helper import UserHelper
from back_api.servises.auth.model.login_response import LoginResponse
from back_api.servises.auth.model.register_request import RegisterRequest
from back_api.servises.general.base_service import BaseService
from back_api.servises.general.models.success_response import SuccessResponse
from back_api.utils.api_utils import ApiUtils


class AuthService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)
        self.authorization_helper = AuthorizationHelper(self.api_utils)
        self.user_helper = UserHelper(self.api_utils)

    def register_user(
            self, register_request: RegisterRequest) -> SuccessResponse:
        response = self.authorization_helper.post_register(
            data=register_request.model_dump())
        return SuccessResponse(**response.json())

    def login_user(self, login_request: RegisterRequest) -> LoginResponse:
        response = self.authorization_helper.post_login(
            data=login_request.model_dump())
        return LoginResponse(**response.json())
