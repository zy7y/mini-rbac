from core.dbhelper import DbHelper


class Service:

    filter_del = {"status__not": 9}

    def __init__(self, dao: DbHelper):
        self.dao = dao

    async def get_items(self, offset, limit):
        """
        分页获取数据, 过滤掉删除
        :param offset: 起始值
        :param limit: 偏移量
        :return:
        """
        skip = (offset - 1) * limit
        return dict(data=await self.dao.selects(skip, limit, Service.filter_del))

    async def query_items(self, query):
        """
        根据条件查询结果
        :param query:
        :return:
        """
        size = query.limit
        skip = (query.offset - 1) * size
        del query.offset, query.limit
        filters = {f"{k}__contains": v for k, v in query.dict().items()}
        filters.update(Service.filter_del)
        return dict(data=await self.dao.selects(skip, size, filters))

    async def delete_item(self, pk):
        """
        逻辑删除数据
        :param pk:主键
        :return:
        """
        filters = {"id": pk}
        filters.update(Service.filter_del)
        if await self.dao.update(filters, {"status": 9}) == 0:
            return dict(code=400, msg="数据不存在")
        return dict()

    async def update_item(self, pk, data):
        """
        更新数据,不通用，可重写
        :param pk: 主键
        :param data: pydantic model
        :return:
        """
        if await self.dao.update({"id": pk}, data.dict()) == 0:
            return dict(code=400, msg="数据不存在")
        return dict()

    async def create_item(self, data):
        """
        创建数据，不通用可重写
        :param data: pydantic model
        :return:
        """
        return await self.dao.insert(data.dict())
