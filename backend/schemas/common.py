"""公共模型"""
from datetime import datetime
from typing import Generic, Optional, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class Response(GenericModel, Generic[T]):
    code: int = 200
    data: Optional[T]
    msg: str = "请求成功"


class ReadBase(BaseModel):
    """数据读取的基类"""

    id: int
    status: int = Field(default=1, description="数据状态 1正常默认值 9 删除 5使用中 ")
    created: datetime
    modified: datetime


class LoginForm(BaseModel):
    """用户登录参数"""

    username: str = Field("admin", description="账号", max_length=12, min_length=3)
    password: str = Field("123456", description="密码", min_length=6, max_length=16)


class LoginResult(BaseModel):
    """登录响应模型"""

    id: int = Field(..., description="用户ID")
    token: str = Field(..., description="token 串")
    token_type: str = Field("Bearer", description="token 类型")


class QueryData(BaseModel):
    """分页查询基础数据"""

    offset: int = Field(default=1, description="页码", ge=1)
    limit: int = Field(default=10, description="数量", ge=1)


class ListAll(GenericModel, Generic[T]):
    """查列表时的模型"""

    total: int = Field(..., description="总数")
    items: T = Field(..., description="数据列表")
