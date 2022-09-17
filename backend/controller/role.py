import json

from fastapi import Query

from core.utils import list_to_tree
from dbhelper.menu import get_menu
from dbhelper.role import (del_role, get_role, get_role_menus, get_roles,
                           new_role, put_role)
from schemas import ListAll, Response, RoleIn, RoleInfo, RoleQuery, RoleRead


async def role_add(data: RoleIn) -> Response[RoleInfo]:
    if result := await new_role(data):
        return Response(data=result)
    return Response(code=400, msg="菜单不存在")


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


async def role_del(pk: int) -> Response:
    if await del_role(pk) == 0:
        return Response(code=400, msg="角色不存在")
    return Response()


async def role_put(pk: int, data: RoleIn) -> Response:
    """更新角色"""
    print(await get_role({"id": pk}))
    if await get_role({"id": pk}) is None:

        return Response(code=400, msg="角色不存在")
    # 如果不为ture -> 有菜单id不存在
    if not all([await get_menu({"id": mid}) for mid in data.menus]):
        return Response(code=400, msg="菜单不存在")

    if await put_role(pk, data) == 0:
        return Response(code=400, msg="角色不存在")
    return Response()


async def role_query(query: RoleQuery) -> Response[ListAll[list[RoleRead]]]:
    """post条件查询角色表"""
    size = query.limit
    skip = (query.offset - 1) * size
    del query.offset, query.limit
    users, count = await get_roles(skip, size, query.dict())
    return Response(data=ListAll(total=count, items=users))
