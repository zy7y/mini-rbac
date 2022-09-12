from core import Response
from dbhelper.menu import insert_menu
from schemas.menu import MenuIn, MenuRead


async def menu_add(data: MenuIn) -> Response[MenuRead]:
    return Response(data=await insert_menu(data))
