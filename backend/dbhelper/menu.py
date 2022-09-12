from models import MenuModel
from schemas.menu import MenuIn


async def insert_menu(menu: MenuIn):
    """新增菜单"""
    return await MenuModel.create(**menu.dict())
