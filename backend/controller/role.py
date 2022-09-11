import json

from core.resp import Response
from core.router import Router
from core.utils import list_to_tree
from dbhelper.role import get_role_menus
from schemas.common import QueryData
from schemas.role import RoleAdd, RoleInfo

role = Router(prefix="/role", tags=["角色管理"])


@role.post("", summary="角色添加")
async def role_add(data: RoleAdd) -> Response[RoleInfo]:
    pass


@role.get("/{pk}", summary="角色详情")
async def role_info(pk: int) -> Response[RoleInfo]:
    pass


@role.delete("/{pk}", summary="删除角色")
async def role_del(pk: int) -> Response:
    pass


@role.put("/{pk}", summary="编辑角色")
async def role_put(pk: int, data: RoleAdd) -> Response[RoleInfo]:
    pass


@role.post("/list", summary="查询角色列表")
async def role_list(data: QueryData) -> Response[list[RoleInfo]]:
    pass


@role.get("/{pk}/menu", summary="查询角色菜单权限")
async def role_menu(pk: int):
    menus = await get_role_menus(pk)
    for obj in menus:
        obj["meta"] = json.loads(obj["meta"]) if obj["meta"] is not None else None
    return Response(data=list_to_tree(menus))


@role.get("/{pk}/menuIds", summary="查询角色菜单ids")
async def role_menus_id():
    pass


@role.get("/assign", summary="分配权限")
async def role_assign():
    pass
