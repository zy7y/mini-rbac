from tortoise.transactions import atomic

from models import RoleModel, UserModel, UserRoleModel
from schemas.user import UserIn, UserRole


async def get_user(kwargs):
    """
    根据条件查询到第一条符合结果的数据
    Args:
        kwargs:

    Returns:

    """
    return await UserModel.filter(**kwargs).first()


async def get_user_info(pk: int):
    """
    根据id查用户角色列表,当前激活角色
    """
    user = await UserModel.get(pk=pk).values(
        "id", "username", "nickname", "identity", "created", "modified"
    )
    role = (
        await UserRoleModel.filter(uid=pk, status__not_in=[9, 5])
        .all()
        .values("rid", "status")
    )
    active_rid = role[0].get("rid")
    rids = []
    for obj in role:
        if obj.get("status") == 5:
            active_rid = obj.get("rid")
        rids.append(obj.get("rid"))
    return {**user, "active_rid": active_rid, "rids": rids}


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
    result = (
        UserModel.filter(status__not_in=[9, 5], **kwargs).all().order_by("-created")
    )
    return await result.offset(skip).limit(limit), await result.count()


@atomic()
async def insert_user(user, roles):
    for index, rid in enumerate(roles):
        # 1. 查角色表是否有该角色
        await RoleModel.get(pk=rid)
        # 创建用户
        obj = await UserModel.create(**user.dict())

        user_role = UserRole(rid=rid, uid=obj.id)
        if index == 0:
            user_role.status = 5
        # 第一个角色默认, 添加到关系表
        await UserRoleModel.create(**user_role.dict())
    return user


async def new_user(user: UserIn):
    """新增用户"""
    return await UserModel.create(**user.dict())
