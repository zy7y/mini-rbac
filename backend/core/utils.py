import importlib
import inspect
import os
import random

from core.log import logger


def list_to_tree(
    menus, parent_flag: str = "pid", children_key: str = "children"
) -> list:
    """
    list 结构转 树结构
    :param menus: [{id:1, pid: 3}]
    :param parent_flag: 节点关系字段
    :param children_key: 生成树结构的子节点字段
    :return: list 类型的 树嵌套数据
    """ ""
    # 先转成字典 id作为key, 数据作为value
    menu_map = {menu["id"]: menu for menu in menus}
    arr = []
    for menu in menus:

        # 有父级
        if mid := menu.get(parent_flag):
            # 有 子项的情况
            if result := menu_map[mid].get(children_key):
                result.append(menu)
            else:
                # 无子项的情况
                menu_map[mid][children_key] = [menu]
        else:
            arr.append(menu)
    return arr


def get_system_info():
    """获取系统信息"""
    return {
        "usage": {
            "cpu": f"{random.random() * 100: .2}",
            "memory": f"{random.random() * 100: .2}",
            "disk": f"{random.random() * 100: .2}",
        },
        "performance": {
            "rps": f"{random.random() * random.randint(1, 50): .2}",
            "time": f"{random.random() * random.randint(1, 50): .2}",
            "user": f"{random.randint(1, 50)}",
        },
    }


def load_routers(
    app,
    package_path: str = "router",
    router_name: str = "router",
    is_init=False,
    no_depends="common",
    depends: list = None,
):
    """
    自动注册路由
    :param app: FastAPI 实例对象 或者 APIRouter对象
    :param package_path: 路由包所在路径，默认相对路径router包
    :param router_name: APIRouter实例名称，需所有实例统一，默认router
    :param is_init: 是否在包中的__init__.py中导入了所有APIRouter实例，默认否
    :param no_depends: 不需要依赖注入的模块（py文件）名，默认common
    :param depends: 依赖注入列表 默认为None
    :return: 默认None
    """

    def __register(module_obj):
        """注册路由，module_obj： 模块对象"""
        if hasattr(module_obj, router_name):
            router_obj = getattr(module_obj, router_name)
            if no_depends in module_obj.__name__:
                kwargs = dict(router=router_obj)
            else:
                kwargs = dict(router=router_obj, dependencies=depends)
            app.include_router(**kwargs)

    logger.info("开始扫描路由。")
    if depends is None:
        depends = []
    if is_init:
        # 1. init 导入了其他自文件包时
        for _, module in inspect.getmembers(
            importlib.import_module(package_path), inspect.ismodule
        ):
            __register(module)

    else:
        # 2. 排除init文件时 的情况
        for _, _, files in os.walk(package_path):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    module = importlib.import_module(f"{package_path}.{file[:-3]}")
                    __register(module)

    for route in app.routes:
        try:
            logger.debug(
                f"{route.path}, {route.methods}, {route.__dict__.get('summary')}"
            )
        except AttributeError as e:
            logger.error(e)
    logger.info("👌路由注册完成✅。")
