from fastapi import APIRouter, Depends

from schemas import common as BaseSchema
from schemas import role as RoleSchema
from schemas.common import QueryData
from service.role import service as RoleService

router = APIRouter(prefix="/role", tags=["角色管理"])

Response = BaseSchema.Response
ListAll = BaseSchema.ListAll

role_list_schema = ListAll[list[RoleSchema.RoleRead]]


@router.get("", summary="角色列表")
async def role_list(query: QueryData = Depends()) -> Response[role_list_schema]:
    return await RoleService.get_items(query.offset, query.limit)


@router.post("/query", summary="角色查询")
async def role_query(query: RoleSchema.RoleQuery) -> Response[role_list_schema]:
    return await RoleService.query_items(query)


@router.post("", summary="角色新增")
async def role_create(data: RoleSchema.RoleIn) -> Response[RoleSchema.RoleInfo]:
    return await RoleService.create_item(data)


@router.get("/{rid}/menu", summary="查询角色拥有权限")
async def role_has_menu(rid: int) -> Response:
    return await RoleService.has_tree_menus(rid)


@router.delete("/{pk}", summary="角色删除")
async def role_del(pk: int) -> Response:
    return await RoleService.delete_item(pk)


@router.put("/{pk}", summary="角色更新")
async def role_put(pk: int, data: RoleSchema.RoleIn) -> Response:
    """更新角色"""
    return await RoleService.update_item(pk, data)
