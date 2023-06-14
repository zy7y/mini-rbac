from fastapi import APIRouter, Depends
from typing import List

from core.middleware import LogRoute
from core.security import check_permissions
from schemas import common as BaseSchema
from schemas import user as UserSchema
from schemas.common import QueryData
from service.user import service as UserService

router = APIRouter(prefix="/user", tags=["用户管理"], route_class=LogRoute)

Response = BaseSchema.Response
ListAll = BaseSchema.ListAll

user_list_schema = ListAll[List[UserSchema.UserRead]]


@router.get("", summary="用户列表")
async def user_list(query: QueryData = Depends()) -> Response[user_list_schema]:
    return await UserService.get_items(query.offset, query.limit)


@router.post("/query", summary="用户查询")
async def user_query(query: UserSchema.UserQuery) -> Response[user_list_schema]:
    return await UserService.query_items(query)


@router.post("", summary="用户新增")
async def user_create(data: UserSchema.UserAdd) -> Response[UserSchema.UserRead]:
    return await UserService.create_item(data)


@router.delete("/{pk}", summary="用户删除")
async def user_delete(pk: int) -> Response:
    return await UserService.delete_item(pk)


@router.get("/{pk}", summary="用户信息")
async def user_info(pk: int) -> Response[UserSchema.UserInfo]:
    return await UserService.get_item(pk)


@router.put("/{pk}", summary="用户更新")
async def user_update(pk: int, data: UserSchema.UserPut) -> Response:
    return await UserService.update_item(pk, data)


@router.put("/role/{rid}", summary="用户切换角色")
async def user_change_role(
    rid: int, user: UserSchema.UserRead = Depends(check_permissions)
) -> Response:
    return await UserService.change_current_role(user.id, rid)
