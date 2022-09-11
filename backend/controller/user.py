from core.resp import Response
from core.router import Router
from dbhelper.user import get_user_info, get_users, insert_user
from schemas.common import ListAll
from schemas.user import UserAdd, UserInfo, UserList, UserQuery

user = Router(prefix="/users", tags=["用户管理"])


@user.post("", summary="用户添加")
async def user_add(data: UserAdd) -> Response[UserInfo]:
    roles = data.rids
    del data.rids
    return await insert_user(data, roles)


@user.get("/{pk}", summary="用户详情")
async def user_info(pk: int) -> Response[UserInfo]:
    try:
        return Response(data=await get_user_info(pk))
    except Exception as e:
        return Response(msg=f"用户不存在 {e}")


@user.delete("/{pk}", summary="删除用户")
async def user_del(pk: int) -> Response:
    pass


@user.put("/{pk}", summary="编辑用户")
async def user_put(pk: int, data: UserAdd) -> Response[UserInfo]:
    pass


@user.post("/list", summary="查询用户列表")
async def user_list(query: UserQuery) -> Response[ListAll[UserList]]:
    limit = query.size
    skip = (query.offset - 1) * limit
    del query.offset, query.size
    users, count = await get_users(skip, limit, query.dict())
    return Response(data=ListAll(total=count, items=users))
