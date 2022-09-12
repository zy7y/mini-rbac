from pydantic import BaseModel, Field
from tortoise.contrib.pydantic import pydantic_model_creator

from core import ReadBase
from models import RoleModel

RoleRed = pydantic_model_creator(RoleModel, name="RoleOut")


class RoleBasic(BaseModel):
    name: str = Field(None, description="角色名称")
    remark: str = Field(None, description="备注信息")


class RoleIn(RoleBasic):
    pass


class RoleRed(RoleBasic, ReadBase):
    pass


class RoleInfo(RoleRed):
    pass
