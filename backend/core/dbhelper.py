"""数据库通用查询方法"""
from typing import Optional

from tortoise import connections, models


class DbHelper:
    def __init__(self, model: models.Model):
        """
        初始化
        :param model: 模型类
        """
        self.model = model

    def __filter(self, kwargs: dict):
        """
        过滤数据,默认过滤数据
        :param kwargs:
        :return:
        """
        return self.model.filter(**kwargs)

    async def select(self, kwargs: dict = None) -> Optional[models.Model]:
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
        self, offset: int, limit: int, kwargs: dict = None, order_by: str = None
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

    async def inserts(self, objs: list[models.Model]):
        """
        批量新增数据
        :param objs: 模型列表
        :return:
        """
        await self.model.bulk_create(objs)

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
