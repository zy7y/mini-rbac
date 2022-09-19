from tortoise import connections

from models import MenuModel, RoleMenuModel, RoleModel
from schemas.role import RoleIn


async def get_role_menus(rid: int):
    """
    根据角色id 获取菜单
    """
    db = connections.get("default")
    # asc 降序
    return await db.execute_query_dict(
        """
        select m.id, m.name, m.icon, m.path, m.type, m.component, m.pid, m.identifier, m.api, m.method
        FROM sys_menu as m, sys_role_menu WHERE m.id = sys_role_menu.mid
        AND sys_role_menu.rid = (?) AND sys_role_menu.`status` = 1 order by m.id asc""",
        [rid],
    )


async def new_role(role: RoleIn):
    """新增角色"""
    # 校验菜单是否存在
    if not all([await MenuModel.filter(id=mid).first() for mid in role.menus]):
        return False

    obj = await RoleModel.create(name=role.name, remark=role.remark)
    # 写入菜单
    await RoleMenuModel.bulk_create(
        [RoleMenuModel(rid=obj.id, mid=mid) for mid in role.menus]
    )
    return obj


async def get_roles(skip: int, limit: int, kwargs: dict = None):
    """
    分页获取用户并且支持字段模糊查询
    Args:
        skip: 偏移量
        limit: 数量
        kwargs: 查询字典

    Returns:

    """
    if kwargs is not None:
        kwargs = {f"{k}__contains": v for k, v in kwargs.items()}
    else:
        kwargs = {}
    result = RoleModel.filter(**kwargs).all().order_by("-created")
    return await result.offset(skip).limit(limit), await result.count()


async def get_role(kwargs):
    """
    根据条件查询到第一条符合结果的数据
    Args:
        kwargs:

    Returns:

    """
    return await RoleModel.filter(**kwargs).first()


async def del_role(rid: int):
    """删除用户"""
    return await RoleModel.filter(id=rid).update(status=9)


async def put_role(pk, data):
    """更新角色 菜单"""
    await RoleModel.filter(id=pk).update(name=data.name, remark=data.remark)
    await RoleMenuModel.filter(rid=pk).update(status=9)

    await RoleMenuModel.bulk_create(
        [RoleMenuModel(rid=pk, mid=mid) for mid in data.menus]
    )
