from Back_API.utils.api_utils import ApiUtils


class BaseService:

    def __init__(self, api_utils: ApiUtils):
        self.api_utils = api_utils