# router service db router+service db
from fastapi import APIRouter

from core.utils import list_to_tree
from dbhelper.menu import (del_menu, get_menu, get_tree_menu, insert_menu,
                           put_menu)
from schemas import MenuIn, MenuRead, Response

router = APIRouter(prefix="/menu", tags=["菜单管理"])


@router.post("", summary="菜单新增", response_model=Response[MenuRead])
async def menu_add(data: MenuIn):
    return Response(data=await insert_menu(data))


@router.get("", summary="菜单列表", response_model=Response)
async def menu_arr():
    menus = await get_tree_menu()
    try:
        data = list_to_tree(menus)
    except KeyError:
        return Response(code=400, msg="菜单根节点丢失")
    return Response(data=data)


@router.delete("/{pk}", summary="菜单删除", response_model=Response)
async def menu_del(pk: int):
    if await get_menu({"pid": pk}) is not None:
        return Response(code=400, msg="请先删除子节点")
    if await del_menu(pk) == 0:
        return Response(code=400, msg="菜单不存在")
    return Response()


@router.put("/{pk}", summary="菜单更新", response_model=Response)
async def menu_put(pk: int, data: MenuIn):
    """更新菜单"""
    if await put_menu(pk, data) == 0:
        return Response(code=400, msg="菜单不存在")
    return Response()
