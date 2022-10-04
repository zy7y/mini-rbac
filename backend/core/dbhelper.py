"""数据库通用查询方法"""
from tortoise import connections

from models import MenuModel, RoleMenuModel, RoleModel, UserModel, UserRoleModel


class DbHelper:
    def __init__(self, model):
        """
        初始化
        :param model: 模型类 orm model
        """
        self.model = model

    def __filter(self, kwargs: dict):
        """
        过滤数据,默认过滤数据
        :param kwargs:
        :return:
        """
        return self.model.filter(**kwargs)

    async def select(self, kwargs: dict = None):
        """
        查询符合条件的第一个对象, 查无结果时返回None
        :param kwargs: kwargs: {"name:"7y", "id": 1}
        :return: select * from model where name = "7y" and id = 1 limit 1
        """
        if kwargs is None:
            kwargs = {}
        return await self.__filter(kwargs).first()

    async def update(self, filters: dict = None, updates: dict = None):
        """
        更新单条数据
        :param filters: 条件字典 {"id":1,"status__not": 9}
        :param updates: 待更新数据 {"status": 5}
        :return: 0 失败， 1 成功
        """
        return await self.__filter(filters).update(**updates)

    async def delete(self, pk: int) -> int:
        """
        逻辑删除单条数据, status -> 9
        :param pk: 数据id
        :return: 0 是删除 失败， 1是删除成功
        """
        filters = {"id": pk}
        updates = dict(status=9)
        return await self.update(filters=filters, updates=updates)

    async def insert(self, data: dict):
        """
        新增一条数据
        :param data: 模型字典
        :return: 新增之后的对象
        """
        return await self.model.create(**data)

    async def selects(
        self, offset: int, limit: int, kwargs: dict = None, order_by: str = "-created"
    ) -> dict:
        """
        条件分页查询数据列表, 支持排序
        Args:
            offset: 偏移量
            limit: 数量
            kwargs: 条件 {}
            order_by: 排序，默认为None， 传入 -字段名 降序 字段名升序
            SQL => select * from model where xx=xx ... order by xx limit offset, limit
        Returns:
            {"items": Model列表, "total": "数量"}
        """
        if kwargs is None:
            kwargs = {}
        objs = self.__filter(kwargs).all()
        if order_by is not None:
            objs = objs.order_by(order_by)

        return dict(
            items=await objs.offset(offset).limit(limit), total=await objs.count()
        )

    async def inserts(self, objs: list):
        """
        批量新增数据
        :param objs: 模型列表
        :return:
        """
        await self.model.bulk_create([self.model(**obj) for obj in objs])

    @classmethod
    async def raw_sql(cls, sql: str, args: list = None):
        """
        手动执行SQL
        :param sql:
        :param args: sql参数
        :return:
        """
        db = connections.get("default")
        if args is None:
            args = []
        return await db.execute_query_dict(sql, args)


UserDao = DbHelper(UserModel)
RoleDao = DbHelper(RoleModel)
UserRoleDao = DbHelper(UserRoleModel)
MenuDao = DbHelper(MenuModel)
RoleMenuDao = DbHelper(RoleMenuModel)


async def has_roles(uid):
    """
    获取用户角色信息,激活的角色升序
    :param uid: 用户id
    :return:
    """
    sql = """select r.id, r.name, ur.status from sys_role as r , sys_user_role as ur where r.id = ur.rid and
             ur.uid = (?) and r.status = 1  and ur.status !=9 order by ur.status desc
            """
    return await UserRoleDao.raw_sql(sql, [uid])


async def has_user(username):
    """
    通过用户名检索数据是否存在
    :param username:
    :return:
    """
    return await UserDao.select({"username": username, "status__not": 9})


async def has_permissions(rid, is_menu=False):
    """
    根据角色ID查到当前拥有的接口权限
    :param rid: 角色ID
    :param is_menu: 是否是菜单，默认不是 -》接口
    :return:
    """
    filters = "m.api, m.method"
    if is_menu:
        filters = "m.id, m.name, m.icon, m.path, m.type, m.component, m.pid, m.identifier, m.api, m.method"
    sql = f"""
        select {filters} 
        FROM sys_menu as m, sys_role_menu as srm WHERE m.id = srm.mid
        AND srm.rid = (?)  and m.status != 9 order by m.id asc"""
    return await RoleMenuDao.raw_sql(sql, [rid])
