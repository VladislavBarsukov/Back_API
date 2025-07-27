from pydantic import BaseModel, ConfigDict
from typing import Literal


class LoginRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    username: str
    password: str
