"""
    Route.post("/role", endpoint=role_add, tags=["角色管理"], summary="角色新增", **has_perm),
    Route.delete(
        "/role/{pk}", endpoint=role_del, tags=["角色管理"], summary="角色删除", **has_perm
    ),
    Route.get(
        "/role/{rid}/menu",
        endpoint=role_has_menu,
        tags=["角色管理"],
        summary="查询角色拥有权限",
        **has_perm
    ),
    Route.put(
        "/role/{pk}", endpoint=role_put, tags=["角色管理"], summary="角色更新", **has_perm
    ),
    Route.post(
        "/role/query", endpoint=role_query, tags=["角色管理"], summary="角色条件查询", **has_perm
    ),
"""

from fastapi import APIRouter, Depends, Query

from core.security import check_permissions
from schemas import common as BaseSchema
from schemas import role as RoleSchema
from service import role as RoleService

router = APIRouter(
    prefix="/role", tags=["角色管理"], dependencies=[Depends(check_permissions)]
)

Response = BaseSchema.Response
ListAll = BaseSchema.ListAll

role_list_schema = ListAll[list[RoleSchema.RoleRead]]


@router.get("", summary="角色列表", response_model=Response[role_list_schema])
async def role_list(
    offset: int = Query(default=1, description="偏移量-页码"),
    limit: int = Query(default=10, description="数据量"),
):
    return await RoleService.get_role_list(offset, limit)


@router.post("/query", summary="角色查询", response_model=Response[role_list_schema])
async def role_query(query: RoleSchema.RoleQuery):
    return await RoleService.query_role_list(query)
