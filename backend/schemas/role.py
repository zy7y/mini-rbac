
from pydantic import Field
from tortoise.contrib.pydantic import pydantic_model_creator

from models import RoleModel

RoleRed = pydantic_model_creator(RoleModel, name="RoleOut")
RoleIn = pydantic_model_creator(RoleModel, name="RoleIn", exclude_readonly=True)


class RoleAdd(RoleIn):
    menus: list[int] = Field(..., description="菜单列表")


class RoleInfo(RoleRed):
    pass
