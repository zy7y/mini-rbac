from core.dbhelper import MenuDao
from core.service import Service
from core.utils import list_to_tree


class MenuService(Service):
    def __init__(self):
        super(MenuService, self).__init__(MenuDao)

    async def get_items(self):
        sql = "select * from sys_menu where status != 9 ;"
        menus = await self.dao.raw_sql(sql)
        try:
            return dict(data=list_to_tree(menus))
        except KeyError:
            return dict(code=400, msg="菜单根节点丢失")

    async def delete_item(self, pk):
        if await MenuDao.select({"pid": pk, "status__not": 9}) is not None:
            return dict(code=400, msg="请先删除子节点")
        if await MenuDao.delete(pk) == 0:
            return dict(code=400, msg="菜单不存在")
        return dict()


service = MenuService()
