from fastapi.encoders import jsonable_encoder
from tortoise import connections

from dbhelper.role import get_role
from models import UserModel, UserRoleModel
from schemas import UserPut


async def get_user(kwargs):
    """
    根据条件查询到第一条符合结果的数据
    Args:
        kwargs:

    Returns:

    """
    return await UserModel.filter(**kwargs).first()


async def get_user_info(user: UserModel):
    """
    根据id查用户角色列表 按激活角色倒序显示
    """
    db = connections.get("default")
    # 查角色表 用户角色表中 角色状态 = 1， 关联表中 状态 != 9  为有效角色
    sql_result = await db.execute_query_dict(
        """
        select r.id, r.name, ur.status from sys_role as r , sys_user_role as ur where r.id = ur.rid and
         ur.uid = (?) and r.status = 1  and ur.status !=9 order by ur.status desc
        """,
        [user.id],
    )
    return {
        **jsonable_encoder(user),
        "roles": sql_result,
    }


async def get_users(skip: int, limit: int, kwargs: dict = None):
    """
    分页获取用户并且支持字段模糊查询
    Args:
        skip: 偏移量
        limit: 数量
        kwargs: 查询字典

    Returns:

    """
    if kwargs is not None:
        kwargs = {f"{k}__contains": v for k, v in kwargs.items()}
    else:
        kwargs = {}
    result = UserModel.filter(**kwargs).all().order_by("-created")
    return await result.offset(skip).limit(limit), await result.count()


async def insert_user(user, roles):
    """新增用户，选择角色"""
    for role in roles:
        if await get_role({"id": role.rid, "status__not": 9}) is None:
            return role.rid

    # 创建用户
    obj = await UserModel.create(**user.dict())
    # 已有角色 关联 角色id 和是否选中状态
    await UserRoleModel.bulk_create(
        [UserRoleModel(rid=role.rid, uid=obj.id, status=role.status) for role in roles]
    )
    return obj


async def del_user(uid: int):
    """删除用户"""
    return await UserModel.filter(id=uid).update(status=9)


async def put_user(uid: int, data: UserPut):
    """更新用户"""
    from core.security import get_password_hash

    rids = data.roles
    del data.roles
    for role in rids:
        if await get_role({"id": role.rid, "status__not": 9}) is None:
            return role.rid
    # 更新用户
    if data.password != "加密之后的密码":
        data.password = get_password_hash(data.password)
    else:
        del data.password
    await UserModel.filter(id=uid).update(**data.dict())

    # todo 1. 先前有的角色，这次更新成没有 2. 先前没有的角色 这次更新成有， 3. 只更新了状态

    db = connections.get("default")
    # 1. 先把用户有的角色做删除
    has_roles = await db.execute_query_dict(
        """
            select r.id from sys_role as r , sys_user_role as ur where r.id = ur.rid and
         ur.uid = (?) and r.status = 1  and ur.status !=9 
    """,
        [uid],
    )

    # 2. 将先有的数据标记 删除
    [await UserRoleModel.filter(rid=role["id"], uid=uid).update(status=9) for role in has_roles]

    # 2. 新增次此更新的数据
    await UserRoleModel.bulk_create(
        [UserRoleModel(uid=uid, **role.dict()) for role in rids]
    )


async def select_role(uid: int, rid: int):
    """用户切换角色"""
    # 1.将用户id 未删除角色状态置为正常 1 （ 除切换角色id ）
    await UserRoleModel.filter(uid=uid, rid__not=rid, status__not=9).update(status=1)
    # 2.将用户id 角色id 和当前角色匹配的数据置为选中
    return await UserRoleModel.filter(uid=uid, rid=rid, status__not=9).update(status=5)
