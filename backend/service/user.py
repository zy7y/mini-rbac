from fastapi.encoders import jsonable_encoder

from core.dbhelper import RoleDao, UserDao, UserRoleDao, has_roles
from core.security import get_password_hash
from core.service import Service


class UserService(Service):
    def __init__(self):
        super(UserService, self).__init__(UserDao)

    async def create_item(self, data):
        """创建用户"""
        # 检查用户是否存在
        if await self.dao.select({"username": data.username}) is not None:
            return dict(code=400, msg="用户名已存在")
        rids = data.roles
        del data.roles
        data.password = get_password_hash(data.password)
        # 检查选中的角色是否存在
        for role in rids:
            if await RoleDao.select(dict(id=role.rid, status__not=9)) is None:
                return dict(code=400, msg=f"角色{role.rid}不存在")

        # 创建用户- 用户表写入数据
        user_obj = await UserDao.insert(data.dict())
        # 关联表写入数据
        await UserRoleDao.inserts(
            [dict(rid=role.rid, uid=user_obj.id, status=role.status) for role in rids]
        )
        return dict(data=user_obj)

    async def get_item(self, pk):
        """获取用户信息"""
        user_obj = await self.dao.select({"id": pk})
        if user_obj is None:
            return dict(code=400, msg="用户不存在")
        roles = await has_roles(user_obj.id)
        return dict(data=dict(**jsonable_encoder(user_obj), roles=roles))

    async def update_item(self, pk, data):
        """用户编辑修改"""
        if await self.dao.select({"id": pk}) is None:
            return dict(code=400, msg="用户不存在")

        rids = data.roles
        del data.roles
        for role in rids:
            if await RoleDao.select({"id": role.rid, "status__not": 9}) is None:
                return role.rid
        # 更新用户
        if data.password != "加密之后的密码":
            data.password = get_password_hash(data.password)
        else:
            del data.password
        await UserDao.update(dict(id=pk), data.dict())

        # todo 1. 先前有的角色，这次更新成没有 2. 先前没有的角色 这次更新成有， 3. 只更新了状态

        roles = await has_roles(pk)

        # 2. 将先有的数据标记 删除
        [
            await UserRoleDao.update(dict(rid=role["id"], uid=pk), dict(status=9))
            for role in roles
        ]

        # 2. 新增次此更新的数据
        await UserRoleDao.inserts(
            [dict(role.dict(), uid=pk, status=role.status) for role in rids]
        )
        return dict()

    @staticmethod
    async def change_current_role(uid, rid):
        """用户切换角色"""
        # 1.将用户id 未删除角色状态置为正常 1 （ 除切换角色id ）
        await UserRoleDao.update(
            dict(uid=uid, rid__not=rid, status__not=9), dict(status=1)
        )
        # 2.将用户id 角色id 和当前角色匹配的数据置为选中
        res = await UserRoleDao.update(
            dict(uid=uid, rid=rid, status__not=9), dict(status=5)
        )
        if res == 0:
            return dict(code=400, msg=f"角色不存在{res}")
        return dict()


service = UserService()
