from fastapi import Query

from core.security import get_password_hash
from dbhelper.user import get_user, get_user_info, get_users, insert_user, new_user
from schemas import Response, UserAdd, UserIn, UserInfo, UserList, UserQuery, UserRead
from schemas.common import ListAll


async def user_add(data: UserAdd) -> Response[UserInfo]:
    """新增用户并分配角色 一步到位"""
    roles = data.rids
    del data.rids
    data.password = get_password_hash(data.password)
    return await insert_user(data, roles)


async def create_user(data: UserIn) -> Response[UserRead]:
    """新增用户"""
    result = await get_user({"username": data.username})
    if result is None:
        data.password = get_password_hash(data.password)
        return Response(data=await new_user(data))
    return Response(msg="用户名已存在")


async def user_info(pk: int) -> Response[UserInfo]:
    try:
        return Response(data=await get_user_info(pk))
    except Exception as e:
        return Response(msg=f"用户不存在 {e}")


async def user_arr(
    offset: int = Query(default=1, description="偏移量-页码"),
    limit: int = Query(default=10, description="数据量"),
) -> Response[ListAll[UserList]]:
    skip = (offset - 1) * limit
    users, count = await get_users(skip, limit)
    return Response(data=ListAll(total=count, items=users))


async def user_list(query: UserQuery) -> Response[ListAll[UserList]]:
    """post查询用户列表"""
    limit = query.size
    skip = (query.offset - 1) * limit
    del query.offset, query.size
    users, count = await get_users(skip, limit, query.dict())
    return Response(data=ListAll(total=count, items=users))
