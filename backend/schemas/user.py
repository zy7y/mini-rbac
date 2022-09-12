from typing import List, Optional

from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

from models import UserRoleModel
from schemas.common import QueryData

UserRole = pydantic_model_creator(UserRoleModel, name="UserRole", exclude_readonly=True)

from schemas.common import ReadBase


class UserBasic(BaseModel):
    username: str
    nickname: str


class UserIn(UserBasic):
    password: str


class UserRead(UserBasic, ReadBase):
    pass


class UserInfo(UserRead):
    active_rid: int = Field(..., description="用户当前激活角色")
    rids: List[int] = Field(..., description="用户拥有角色")


class UserAdd(UserIn):
    rids: List[int] = Field(..., description="用户角色列表")


class UserQuery(QueryData):
    username: Optional[str] = Field("", description="用户名")
    nickname: Optional[str] = Field("", description="姓名")


UserList = List[UserRead]
