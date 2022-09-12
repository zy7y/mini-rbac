import json

from core.utils import list_to_tree
from dbhelper.role import get_role_menus, new_role
from schemas import Response, RoleIn, RoleInfo


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
