from pydantic import BaseModel, Field

from schemas.common import QueryData, ReadBase


class RoleMenuIn(BaseModel):
    """角色 -分配菜单id"""

    rid: int = Field(description="角色ID")
    menus: list[int] = Field(description="菜单ID 列表")


class RoleMenuRead(RoleMenuIn, ReadBase):
    pass


class RoleBasic(BaseModel):
    name: str = Field(None, description="角色名称")
    remark: str = Field(None, description="备注信息")


class RoleIn(RoleBasic):
    menus: list[int] = Field(..., description="菜单id列表")


class RoleRead(RoleBasic, ReadBase):
    pass


class RoleInfo(RoleRead):
    pass


class RoleQuery(QueryData):
    """查询模型"""

    name: str = Field("", description="角色名")
