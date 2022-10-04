from fastapi import APIRouter, Depends, Query

from core.security import check_permissions, get_password_hash
from dbhelper.user import (del_user, get_user, get_user_info, get_users,
                           insert_user, put_user, select_role)
from schemas import Response, UserAdd, UserInfo, UserPut, UserQuery, UserRead
from schemas.common import ListAll

router = APIRouter(prefix="/user", tags=["用户管理"])


@router.post("", summary="用户新增", response_model=Response[UserRead])
async def user_add(data: UserAdd):
    """新增用户并分配角色 一步到位"""
    if await get_user({"username": data.username}) is not None:
        return Response(code=400, msg="用户名已存在")
    rids = data.roles
    del data.roles
    data.password = get_password_hash(data.password)
    result = await insert_user(data, rids)
    if isinstance(result, int):
        return Response(code=400, msg=f"角色{result}不存在")
    return Response(data=result)


@router.get("/{pk}", summary="用户信息", response_model=Response[UserInfo])
async def user_info(pk: int):
    """获取用户信息"""
    obj = await get_user({"id": pk})
    if obj is None:
        return Response(code=400, msg="用户不存在")
    return Response(data=await get_user_info(obj))


@router.get("", summary="用户列表", response_model=Response[ListAll[list[UserRead]]])
async def user_arr(
    offset: int = Query(default=1, description="偏移量-页码"),
    limit: int = Query(default=10, description="数据量"),
):
    """分页列表数据"""
    skip = (offset - 1) * limit
    users, count = await get_users(skip, limit)
    return Response(data=ListAll(total=count, items=users))


@router.post("/query", summary="用户查询", response_model=Response[ListAll[list[UserRead]]])
async def user_list(query: UserQuery):
    """post查询用户列表"""
    size = query.limit
    skip = (query.offset - 1) * size
    del query.offset, query.limit
    users, count = await get_users(skip, size, query.dict())
    return Response(data=ListAll(total=count, items=users))


@router.delete("/{pk}", summary="用户删除", response_model=Response)
async def user_del(pk: int):
    """删除用户"""
    if await del_user(pk) == 0:
        return Response(code=400, msg="用户不存在")
    return Response()


@router.put("/{pk}", summary="用户更新", response_model=Response)
async def user_put(pk: int, data: UserPut):
    """更新用户"""
    if await get_user({"id": pk}) is None:
        return Response(code=400, msg="用户不存在")

    result = await put_user(pk, data)
    if isinstance(result, int):
        return Response(code=400, msg=f"角色不存在{result}")
    return Response()


@router.put("/role/{rid}", summary="用户切换角色", response_model=Response)
async def user_select_role(rid: int, user=Depends(check_permissions)):
    """用户切换角色"""
    res = await select_role(user.id, rid)
    if res == 0:
        return Response(code=400, msg=f"角色不存在{res}")
    return Response()
