from fastapi import APIRouter, Depends, Query

from core.security import check_permissions
from schemas import common as BaseSchema
from schemas import user as UserSchema
from service.user import service as UserService

router = APIRouter(prefix="/user", tags=["用户管理"])

Response = BaseSchema.Response
ListAll = BaseSchema.ListAll

user_list_schema = ListAll[list[UserSchema.UserRead]]


@router.get("", summary="用户列表", response_model=Response[user_list_schema])
async def user_list(
    offset: int = Query(default=1, description="偏移量-页码"),
    limit: int = Query(default=10, description="数据量"),
):
    return await UserService.get_items(offset, limit)


@router.post("/query", summary="用户查询", response_model=Response[user_list_schema])
async def user_query(query: UserSchema.UserQuery):
    return await UserService.query_items(query)


@router.post("", summary="用户新增", response_model=Response[UserSchema.UserRead])
async def user_create(data: UserSchema.UserAdd):
    return await UserService.create_item(data)


@router.delete("/{pk}", summary="用户删除", response_model=Response)
async def user_delete(pk: int):
    return await UserService.delete_item(pk)


@router.get("/{pk}", summary="用户信息", response_model=Response[UserSchema.UserInfo])
async def user_info(pk: int):
    return await UserService.get_item(pk)


@router.put("/{pk}", summary="用户更新", response_model=Response)
async def user_update(pk: int, data: UserSchema.UserPut):
    return await UserService.update_item(pk, data)


@router.put("/role/{rid}", summary="用户切换角色", response_model=Response)
async def user_change_role(
    rid: int, user: UserSchema.UserRead = Depends(check_permissions)
):
    return await UserService.change_current_role(user.id, rid)
