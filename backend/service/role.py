from core.dbhelper import MenuDao, RoleDao, RoleMenuDao, has_permissions
from core.service import Service
from core.utils import list_to_tree


class RoleService(Service):
    def __init__(self):
        super(RoleService, self).__init__(RoleDao)

    async def create_item(self, role):
        """
        创建角色
        :param role: pydantic model
        :return:
        """
        if not all(
            [await MenuDao.select({"id": mid, "status__not": 9}) for mid in role.menus]
        ):
            return dict(code=400, msg="菜单不存在")

        obj = await RoleDao.insert(dict(name=role.name, remark=role.remark))
        # 写入菜单
        await RoleMenuDao.inserts([dict(rid=obj.id, mid=mid) for mid in role.menus])
        return dict(data=obj)

    async def update_item(self, pk, data):
        """
        更新角色
        :param pk:
        :param data:
        :return:
        """
        if await RoleDao.select({"id": pk}) is None:
            return dict(code=400, msg="角色不存在")
        # 如果不为ture -> 有菜单id不存在
        if not all([await MenuDao.select({"id": mid}) for mid in data.menus]):
            return dict(code=400, msg="菜单不存在")

        await RoleDao.update(dict(id=pk), dict(name=data.name, remark=data.remark))
        await RoleMenuDao.update(dict(rid=pk), dict(status=9))

        await RoleMenuDao.inserts([dict(rid=pk, mid=mid) for mid in data.menus])

        return dict()

    @staticmethod
    async def has_tree_menus(pk):
        """
        查询角色拥有菜单
        :param pk:
        :return:
        """
        menus = await has_permissions(pk, is_menu=True)

        try:
            return dict(data=list_to_tree(menus))
        except KeyError:
            return dict(code=400, msg="菜单缺少根节点.")


service = RoleService()
