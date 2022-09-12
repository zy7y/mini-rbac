from tortoise import connections

from dbhelper.menu import get_menu
from models import RoleMenuModel, UserRoleModel
from schemas import UserRole


async def user_assigned_role(data: UserRole):
    """给用户分配角色"""
    return await UserRoleModel.create(**data.dict())


async def role_assigned_menu(data):
    """给角色分配菜单"""
    for mid in data.menus:
        if await get_menu({"id": mid}) is None:
            return mid

    # todo 性能优化
    db = connections.get("default")
    # 1. 先把所有数据做删除
    await db.execute_query_dict(
        """
    update sys_role_menu set status = 9 where rid = (?)
    """,
        [data.rid],
    )
    # 2. 新增数据
    await RoleMenuModel.bulk_create(
        [RoleMenuModel(rid=data.rid, mid=mid) for mid in data.menus]
    )
