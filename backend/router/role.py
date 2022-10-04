from fastapi import APIRouter, Query

from schemas import common as BaseSchema
from schemas import role as RoleSchema
from service.role import service as RoleService

router = APIRouter(prefix="/role", tags=["角色管理"])

Response = BaseSchema.Response
ListAll = BaseSchema.ListAll

role_list_schema = ListAll[list[RoleSchema.RoleRead]]


@router.get("", summary="角色列表", response_model=Response[role_list_schema])
async def role_list(
    offset: int = Query(default=1, description="偏移量-页码"),
    limit: int = Query(default=10, description="数据量"),
):
    return await RoleService.get_items(offset, limit)


@router.post("/query", summary="角色查询", response_model=Response[role_list_schema])
async def role_query(query: RoleSchema.RoleQuery):
    return await RoleService.query_items(query)


@router.post("", summary="角色新增", response_model=Response[RoleSchema.RoleInfo])
async def role_create(data: RoleSchema.RoleIn):
    return await RoleService.create_item(data)


@router.get("/{rid}/menu", summary="查询角色拥有权限", response_model=Response)
async def role_has_menu(rid: int):
    return await RoleService.has_tree_menus(rid)


@router.delete("/{pk}", summary="角色删除", response_model=Response)
async def role_del(pk: int):
    return await RoleService.delete_item(pk)


@router.put("/{pk}", summary="角色更新", response_model=Response)
async def role_put(pk: int, data: RoleSchema.RoleIn):
    """更新角色"""
    return await RoleService.update_item(pk, data)
