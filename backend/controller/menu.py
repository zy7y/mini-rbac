from fastapi import Query

from core.utils import list_to_tree
from dbhelper.menu import del_menu, get_menus, get_tree_menu, insert_menu, put_menu
from schemas import ListAll, MenuIn, MenuRead, Response


async def menu_add(data: MenuIn) -> Response[MenuRead]:
    return Response(data=await insert_menu(data))


async def menu_arr(
    offset: int = Query(default=1, description="偏移量"),
    limit: int = Query(default=10, description="数量"),
) -> Response:
    menus = await get_tree_menu()
    return Response(data=list_to_tree(menus))


async def menu_del(pk: int) -> Response:
    if await del_menu(pk) == 0:
        return Response(code=400, msg="菜单不存在")
    return Response()


async def menu_put(pk: int, data: MenuIn) -> Response:
    """更新菜单"""
    if await put_menu(pk, data) == 0:
        return Response(code=400, msg="菜单不存在")
    return Response()
