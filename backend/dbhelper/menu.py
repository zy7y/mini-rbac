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
    return await result.offset(skip).limit(limit), await result.count()


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
