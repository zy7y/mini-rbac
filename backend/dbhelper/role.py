from tortoise import connections

from models import RoleModel
from schemas.role import RoleIn


async def get_role_menus(rid: int):
    """
    根据角色id 获取菜单
    """
    db = connections.get("default")
    return await db.execute_query_dict(
        """
        select m.id, m.name, m.meta, m.path, m.type, m.component, m.pid, m.identifier, m.api_regx,m.api, m.method, m.sort 
        FROM sys_menu as m, sys_role_menu WHERE m.id = sys_role_menu.mid
        AND sys_role_menu.rid = (%s) AND m.`status` = 1 ORDER BY m.sort""",
        [rid],
    )


async def new_role(role: RoleIn):
    """新增角色"""
    return await RoleModel.create(**role.dict())
