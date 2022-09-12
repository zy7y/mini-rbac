from typing import Optional

from pydantic import BaseModel, Field

from schemas.common import ReadBase


class MenuBasic(BaseModel):
    name: str
    meta: dict = Field(default=None, description="元信息")
    path: Optional[str] = Field(default=None, description="前端路由地址")
    type: int = Field(description="0 目录 1 组件 2 按钮")
    component: Optional[str] = Field(default=None, description="前端组件地址")
    pid: int = Field(default=0, description="0 表示没有根节点")
    identifier: Optional[str] = Field(default=None, description="权限标识符 -> 按钮显示")
    api: Optional[str] = Field(default=None, description="后端接口地址")
    method: Optional[str] = Field(default=None, description="接口请求方法")
    regx: Optional[str] = Field(default=None, description="正则匹配")


class MenuIn(MenuBasic):
    pass


class MenuRead(MenuBasic, ReadBase):
    pass
