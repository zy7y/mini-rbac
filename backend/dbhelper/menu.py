from tortoise import connections

from models import MenuModel
from schemas.menu import MenuIn


async def insert_menu(menu: MenuIn):
    """新增菜单"""
    return await MenuModel.create(**menu.dict())


async def get_menus(skip: int, limit: int, kwargs: dict = None):
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
    result = MenuModel.filter(status__not=9, **kwargs).all().order_by("-created")
    return await result.offset(skip).limit(limit)


async def get_tree_menu():
    return await MenuModel.filter(status__not=9).all().values()


async def get_menu(kwargs):
    """
    根据条件查询到第一条符合结果的数据
    Args:
        kwargs:

    Returns:

    """
    return await MenuModel.filter(**kwargs).first()


async def del_menu(mid: int):
    """删除用户"""
    return await MenuModel.filter(id=mid).update(status=9)


async def get_apis(pk: int):
    """返回当前角色拥有的接口权限列表"""
    db = connections.get("default")
    return await db.execute_query_dict(
        """
        select m.api, m.method
        FROM sys_menu as m, sys_role_menu as srm WHERE m.id = srm.mid
        AND srm.rid = (?)  and m.status != 9""",
        [pk],
    )


async def put_menu(pk: int, data):
    """更新菜单"""
    return await MenuModel.filter(id=pk).update(**data.dict())
