from fastapi import Query

from core.security import get_password_hash
from dbhelper.user import (del_user, get_user, get_user_info, get_users,
                           insert_user, put_user)
from schemas import Response, UserAdd, UserInfo, UserPut, UserQuery, UserRead
from schemas.common import ListAll


async def user_add(data: UserAdd) -> Response[UserRead]:
    """新增用户并分配角色 一步到位"""
    if await get_user({"username": data.username}) is not None:
        return Response(code=400, msg="用户名已存在")
    roles = data.rids
    del data.rids
    data.password = get_password_hash(data.password)
    result = await insert_user(data, roles)
    if isinstance(result, int):
        return Response(code=400, msg=f"角色{result}不存在")
    return Response(data=result)


async def user_info(pk: int) -> Response[UserInfo]:
    """获取用户信息"""
    obj = await get_user({"id": pk})
    if obj is None:
        return Response(code=400, msg="用户不存在")
    return Response(data=await get_user_info(obj))


async def user_arr(
    offset: int = Query(default=1, description="偏移量-页码"),
    limit: int = Query(default=10, description="数据量"),
) -> Response[ListAll[list[UserRead]]]:
    """分页列表数据"""
    skip = (offset - 1) * limit
    users, count = await get_users(skip, limit)
    return Response(data=ListAll(total=count, items=users))


async def user_list(query: UserQuery) -> Response[ListAll[list[UserRead]]]:
    """post查询用户列表"""
    limit = query.size
    skip = (query.offset - 1) * limit
    del query.offset, query.size
    users, count = await get_users(skip, limit, query.dict())
    return Response(data=ListAll(total=count, items=users))


async def user_del(pk: int) -> Response:
    """删除用户"""
    if await del_user(pk) == 0:
        return Response(code=400, msg="用户不存在")
    return Response()


async def user_put(pk: int, data: UserPut) -> Response:
    """更新用户"""
    if await get_user({"id": pk}) is None:
        return Response(code=400, msg="用户不存在")

    result = await put_user(pk, data)
    if isinstance(result, int):
        return Response(code=400, msg=f"角色不存在{result}")
    return Response()
