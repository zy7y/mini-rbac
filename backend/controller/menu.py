from dbhelper.menu import insert_menu
from schemas import MenuIn, MenuRead, Response


async def menu_add(data: MenuIn) -> Response[MenuRead]:
    return Response(data=await insert_menu(data))
