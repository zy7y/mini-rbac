from core.security import get_password_hash
from dbhelper import user as UserDao


async def get_user_list(offset, limit):
    """获取用户列表"""
    skip = (offset - 1) * limit
    users, count = await UserDao.get_users(skip, limit)
    return dict(data=dict(total=count, items=users))


async def query_user_list(query):
    """查询用户列表"""
    size = query.limit
    skip = (query.offset - 1) * size
    del query.offset, query.limit
    users, count = await UserDao.get_users(skip, size, query.dict())
    return dict(data=dict(total=count, items=users))


async def user_create(data):
    """创建用户"""
    if await UserDao.get_user({"username": data.username}) is not None:
        return dict(code=400, msg="用户名已存在")
    rids = data.roles
    del data.roles
    data.password = get_password_hash(data.password)
    result = await UserDao.insert_user(data, rids)
    if isinstance(result, int):
        return dict(code=400, msg=f"角色{result}不存在")
    return dict(data=result)


async def user_delete(pk):
    """逻辑删除用户"""
    if await UserDao.del_user(pk) == 0:
        return dict(code=400, msg="用户不存在")
    return dict()


async def user_info(pk):
    """获取用户信息"""
    obj = await UserDao.get_user({"id": pk})
    if obj is None:
        return dict(code=400, msg="用户不存在")
    return dict(data=await UserDao.get_user_info(obj))


async def user_edit(pk, data):
    """用户编辑修改"""
    if await UserDao.get_user({"id": pk}) is None:
        return dict(code=400, msg="用户不存在")

    result = await UserDao.put_user(pk, data)
    if isinstance(result, int):
        return dict(code=400, msg=f"角色不存在{result}")
    return dict()


async def change_current_role(uid, rid):
    """用户切换角色"""
    res = await UserDao.select_role(uid, rid)
    if res == 0:
        return dict(code=400, msg=f"角色不存在{res}")
    return dict()
