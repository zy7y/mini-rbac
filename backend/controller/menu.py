from core.resp import Response
from core.router import Router
from schemas.common import QueryData
from schemas.menu import MenuIn, MenuRead

menu = Router(prefix="/menu", tags=["菜单管理"])


@menu.post("", summary="菜单添加")
async def menu_add(data: MenuIn) -> Response[MenuRead]:
    pass


@menu.get("/{pk}", summary="菜单详情")
async def menu_info(pk: int) -> Response[MenuRead]:
    pass


@menu.delete("/{pk}", summary="删除菜单")
async def menu_del(pk: int) -> Response:
    pass


@menu.put("/{pk}", summary="编辑菜单")
async def menu_put(pk: int, data: MenuIn) -> Response[MenuRead]:
    pass


@menu.post("/list", summary="查询菜单列表")
async def menu_list(data: QueryData) -> Response[list[MenuRead]]:
    pass
