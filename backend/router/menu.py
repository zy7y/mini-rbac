from fastapi import APIRouter

from schemas import common as BaseSchema
from schemas import menu as MenuSchema
from service.menu import service as MenuService

router = APIRouter(prefix="/menu", tags=["菜单管理"])

Response = BaseSchema.Response


@router.post("", summary="菜单新增", response_model=Response[MenuSchema.MenuRead])
async def menu_add(data: MenuSchema.MenuIn):
    return await MenuService.create_item(data)


@router.get("", summary="菜单列表", response_model=Response)
async def menu_arr():
    return await MenuService.get_items()


@router.delete("/{pk}", summary="菜单删除", response_model=Response)
async def menu_del(pk: int):
    return await MenuService.delete_item(pk)


@router.put("/{pk}", summary="菜单更新", response_model=Response)
async def menu_put(pk: int, data: MenuSchema.MenuIn):
    """更新菜单"""
    return await MenuService.update_item(pk, data)
