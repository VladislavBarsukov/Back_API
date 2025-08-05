from pydantic import BaseModel, ConfigDict


class SuccessResponse(BaseModel):
    detail: str
