"""公共模型"""
from typing import Generic, TypeVar

from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar("T")


class LoginForm(BaseModel):
    """用户登录参数"""

    username: str = Field(..., description="账号", max_length=12, min_length=3)
    password: str = Field(..., description="密码", min_length=6, max_length=16)


class LoginResult(BaseModel):
    """登录响应模型"""

    id: int = Field(..., description="用户ID")
    access_token: str = Field(..., description="token 串")
    token_type: str = Field("Bearer", description="token 类型")


class QueryData(BaseModel):
    """分页查询基础数据"""

    offset: int = 1
    size: int = 10


class ListAll(GenericModel, Generic[T]):
    """查列表时的模型"""

    total: int = Field(..., description="总数")
    items: T = Field(..., description="数据列表")
