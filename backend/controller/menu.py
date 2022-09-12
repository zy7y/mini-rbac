from fastapi import Query

from dbhelper.menu import del_menu, get_menus, insert_menu
from schemas import ListAll, MenuIn, MenuRead, Response


async def menu_add(data: MenuIn) -> Response[MenuRead]:
    return Response(data=await insert_menu(data))


async def menu_arr(
    offset: int = Query(default=1, description="偏移量"),
    limit: int = Query(default=10, description="数量"),
) -> Response[ListAll[list[MenuRead]]]:
    skip = (offset - 1) * limit
    menus, count = await get_menus(skip, limit)
    return Response(data=ListAll(total=count, items=menus))


async def menu_del(pk: int) -> Response:
    if await del_menu(pk) == 0:
        return Response(code=400, msg="菜单不存在")
    return Response()
