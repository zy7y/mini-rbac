from fastapi import APIRouter, Query

from core.utils import list_to_tree
from dbhelper.menu import get_menu
from dbhelper.role import (del_role, get_role, get_role_menus, get_roles,
                           new_role, put_role)
from schemas import ListAll, Response, RoleIn, RoleInfo, RoleQuery, RoleRead

router = APIRouter(prefix="/role", tags=["角色管理"])


@router.post("", summary="角色新增", response_model=Response[RoleInfo])
async def role_add(data: RoleIn):
    if result := await new_role(data):
        return Response(data=result)
    return Response(code=400, msg="菜单不存在")


@router.get("/{rid}/menu", summary="查询角色拥有权限", response_model=Response)
async def role_has_menu(rid: int):
    """
    rid: 角色ID
    """
    menus = await get_role_menus(rid)

    try:
        result = list_to_tree(menus)
    except KeyError:
        return Response(code=400, msg="菜单缺少根节点.")
    return Response(data=result)


@router.get("", summary="角色列表", response_model=Response[ListAll[list[RoleRead]]])
async def role_arr(
    offset: int = Query(default=1, description="偏移量-页码"),
    limit: int = Query(default=10, description="数据量"),
):
    skip = (offset - 1) * limit
    roles, count = await get_roles(skip, limit)
    return Response(data=ListAll(total=count, items=roles))


@router.delete("/{pk}", summary="角色删除", response_model=Response)
async def role_del(pk: int):
    if await del_role(pk) == 0:
        return Response(code=400, msg="角色不存在")
    return Response()


@router.put("/{pk}", summary="角色更新", response_model=Response)
async def role_put(pk: int, data: RoleIn):
    """更新角色"""
    if await get_role({"id": pk}) is None:

        return Response(code=400, msg="角色不存在")
    # 如果不为ture -> 有菜单id不存在
    if not all([await get_menu({"id": mid}) for mid in data.menus]):
        return Response(code=400, msg="菜单不存在")

    if await put_role(pk, data) == 0:
        return Response(code=400, msg="角色不存在")
    return Response()


@router.post("/query", summary="角色查询", response_model=Response[ListAll[list[RoleRead]]])
async def role_query(query: RoleQuery):
    """post条件查询角色表"""
    size = query.limit
    skip = (query.offset - 1) * size
    del query.offset, query.limit
    users, count = await get_roles(skip, size, query.dict())
    return Response(data=ListAll(total=count, items=users))
