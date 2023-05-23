from pydantic import BaseModel, Field


class UserDataModel(BaseModel):
    username: str = Field(
        description="The login username of the user", default="")
    email: str = Field(
        description="The login email of the user", default="")
    password: str = Field(
        description="The login password of the user", default="")
    isActive: bool = Field(
        description="The login password of the user", default=False)
    userLevel: str = Field(
        description="The login password of the user", default="1")
