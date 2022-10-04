from dbhelper import role as RoleDao


async def get_role_list(offset, limit):
    """
    分页获取角色列表数据
    :param offset: 偏移
    :param limit: 显示数量
    :return:
    """

    skip = (offset - 1) * limit
    roles, count = await RoleDao.get_roles(skip, limit)
    return dict(data=dict(total=count, items=roles))


async def query_role_list(query):
    """
    条件查询角色列表
    :param query: RoleQuery Schema
    :return:
    """

    size = query.limit
    skip = (query.offset - 1) * size
    del query.offset, query.limit
    users, count = await RoleDao.get_roles(skip, size, query.dict())
    return dict(data=dict(total=count, items=users))
