import pytest
import requests as client

from core.log import logger
from schemas.menu import MenuIn
from schemas.role import RoleIn
from schemas.user import RoleActive, UserAdd

base = "http://localhost:8000"


dirs = [
    (
        "/menu",
        MenuIn(  # id 1
            name="系统管理",
            meta={"icon": "AppstoreOutlined"},
            path="/system",
            type=0,
            component=None,
            pid=0,
            identifier=None,
            api=None,
            method=None,
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(  # id 2
            name="系统设置",
            meta={"icon": "SettingOutlined"},
            path="/system",
            type=0,
            component=None,
            pid=0,
            identifier=None,
            api=None,
            method=None,
        ).dict(),
    ),
]


@pytest.mark.parametrize("path, data", dirs)
def test_add_dir(path, data):
    """添加一级目录"""
    res = client.post(url=base + path, json=data)
    logger.info(res.json())
    assert res.status_code == 200


menus = [
    (
        "/menu",
        MenuIn(  # id 3
            name="用户管理",
            meta={"icon": "TeamOutlined", "title": "用户管理"},
            path="/system/user",
            type=1,
            component="/system/user/user.vue",
            pid=1,
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(  # id 4
            name="角色管理",
            meta={"icon": "UserOutlined", "title": "角色管理"},
            path="/system/role",
            type=1,
            component="/system/role/role.vue",
            pid=1,
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(  # id 5
            name="菜单管理",
            meta={"icon": "MenuOutlined", "title": "菜单管理"},
            path="/system/menu",
            type=1,
            component="/system/menu/menu.vue",
            pid=1,
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(  # id 6
            name="关于",
            meta={"icon": "DashboardOutlined", "title": "关于"},
            path="/setting/about",
            type=1,
            component="/setting/about/about.vue",
            pid=2,
        ).dict(),
    ),
]


@pytest.mark.parametrize("path,data", menus)
def test_add_menu(path, data):
    """添加二级菜单"""
    res = client.post(url=base + path, json=data)
    logger.info(res.json())
    assert res.status_code == 200


user_manager_pre = [
    MenuIn(
        name="用户详情",
        type=3,
        identifier="user:get",
        api="/user/{pk}",
        method="GET",
    ),
    MenuIn(
        name="用户列表",
        type=3,  # 数据类
        api="/user",
        method="GET",
    ),
    MenuIn(
        name="用户查询",
        type=2,
        identifier="user:query",
        api="/user/query",
        method="POST",
    ),
    MenuIn(
        name="用户新增",
        type=2,
        identifier="user:create",
        api="/user",
        method="POST",
    ),
    MenuIn(
        name="用户删除",
        type=2,
        identifier="user:delete",
        api="/user/{pk}",
        method="DELETE",
    ),
    MenuIn(
        name="用户更新",
        type=2,
        identifier="user:update",
        api="/user/{pk}",
        method="PUT",
    ),
]


@pytest.mark.parametrize("data", user_manager_pre)
def test_add_user_pre(data):
    """用户管理相关权限"""
    data.pid = 3
    res = client.post(url=base + "/menu", json=data.dict())
    logger.info(res.json())
    assert res.status_code == 200


role_manager_pre = [
    MenuIn(
        name="查询角色拥有权限",
        type=3,
        api="/role/{rid}/menu",
        method="GET",
    ),
    MenuIn(
        name="角色列表",
        type=3,
        api="/role",
        method="GET",
    ),
    MenuIn(
        name="角色查询",
        meta={"icon": "Search"},
        type=2,
        identifier="role:query",
        api="/role/query",
        method="POST",
    ),
    MenuIn(
        name="角色新增",
        type=2,
        identifier="role:create",
        api="/role",
        method="POST",
    ),
    MenuIn(
        name="角色删除",
        type=2,
        identifier="role:delete",
        api="/role/{pk}",
        method="DELETE",
    ),
    MenuIn(
        name="角色更新",
        type=2,
        identifier="role:update",
        api="/role/{pk}",
        method="PUT",
    ),
]


@pytest.mark.parametrize("data", role_manager_pre)
def test_add_role_pre(data):
    """角色管理相关权限"""
    logger.debug(data.dict())
    data.pid = 4
    res = client.post(url=base + "/menu", json=data.dict())
    logger.info(res.json())
    assert res.status_code == 200


menu_manager_pre = [
    MenuIn(
        name="菜单列表",
        type=3,
        api="/menu",
        method="GET",
    ),
    MenuIn(
        name="菜单新增",
        type=2,
        identifier="menu:create",
        api="/menu",
        method="POST",
    ),
    MenuIn(
        name="菜单更新",
        type=2,
        identifier="menu:update",
        api="/menu/{pk}",
        method="PUT",
    ),
    MenuIn(
        name="菜单删除",
        type=2,
        identifier="menu:delete",
        api="/menu/{pk}",
        method="DELETE",
    ),
]


@pytest.mark.parametrize("data", menu_manager_pre)
def test_add_menu_pre(data):
    """菜单管理相关权限"""
    data.pid = 5
    res = client.post(url=base + "/menu", json=data.dict())
    logger.info(res.json())
    assert res.status_code == 200


menus_len = (
    len(user_manager_pre)
    + len(menus)
    + len(dirs)
    + len(role_manager_pre)
    + len(menu_manager_pre)
)

datas = [
    (
        "/role",
        RoleIn(
            name="superStar",
            remark="全部权限",
            menus=[num for num in range(1, menus_len)],
        ),
    ),
    # 创建用户
    (
        "/user",
        UserAdd(
            username="admin",
            nickname="666管理员",
            password="123456",
            roles=[RoleActive(rid=1, status=5)],
        ),
    ),
]


@pytest.mark.parametrize("path, data", datas)
def test_add_user(path, data):
    """添加账号"""
    res = client.post(url=base + path, json=data.dict())
    logger.info(res.json())
    logger.info(menus_len)
    assert res.status_code == 200
