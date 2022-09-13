import json

from fastapi import Query

from core.utils import list_to_tree
from dbhelper.relation import role_assigned_menu
from dbhelper.role import (del_role, get_role, get_role_menus, get_roles,
                           new_role, put_role)
from schemas import (ListAll, Response, RoleIn, RoleInfo, RoleMenuIn,
                     RoleQuery, RoleRead)


async def role_add(data: RoleIn) -> Response[RoleInfo]:
    return Response(data=await new_role(data))


async def role_has_menu(rid: int):
    """
    rid: 角色ID
    """
    menus = await get_role_menus(rid)
    for obj in menus:
        obj["meta"] = json.loads(obj["meta"]) if obj["meta"] is not None else None
    return Response(data=list_to_tree(menus))


async def role_arr(
    offset: int = Query(default=1, description="偏移量-页码"),
    limit: int = Query(default=10, description="数据量"),
) -> Response[ListAll[list[RoleRead]]]:
    skip = (offset - 1) * limit
    roles, count = await get_roles(skip, limit)
    return Response(data=ListAll(total=count, items=roles))


async def assigned_menu(data: RoleMenuIn) -> Response:
    """分配菜单给角色"""
    if await get_role({"id": data.rid, "status__not": 9}) is None:
        return Response(code=400, msg="角色不存在")
    if isinstance(await role_assigned_menu(data), int):
        return Response(code=400, msg=f"菜单不存在")
    return Response()


async def role_del(pk: int) -> Response:
    if await del_role(pk) == 0:
        return Response(code=400, msg="角色不存在")
    return Response()


async def role_put(pk: int, data: RoleIn) -> Response:
    """更新角色"""
    if await put_role(pk, data) == 0:
        return Response(code=400, msg="角色不存在")
    return Response()


async def role_query(query: RoleQuery) -> Response[ListAll[list[RoleRead]]]:
    """post条件查询角色表"""
    limit = query.size
    skip = (query.offset - 1) * limit
    del query.offset, query.size
    users, count = await get_roles(skip, limit, query.dict())
    return Response(data=ListAll(total=count, items=users))
