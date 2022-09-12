from tortoise import Tortoise


async def init_orm():
    """初始化orm"""
    await Tortoise.init(db_url="sqlite://mini.db", modules={"models": ["models"]})
    await Tortoise.generate_schemas()


async def close_orm():
    """关闭orm"""
    await Tortoise.close_connections()
