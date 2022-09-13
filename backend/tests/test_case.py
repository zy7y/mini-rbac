import pytest
import requests as client

from core.log import logger
from schemas.menu import MenuIn
from schemas.role import RoleIn, RoleMenuIn
from schemas.user import RoleActive, UserAdd

base = "http://localhost:8000"


params = [
    # 创建角色
    ("/role", RoleIn(name="super", remark="全部权限").dict()),
    ("/role", RoleIn(name="user", remark="用户权限").dict()),
    # 创建用户
    (
        "/user",
        UserAdd(
            username="admin",
            nickname="管理员",
            password="123456",
            rids=[
                RoleActive(rid=1, status=5),
                RoleActive(rid=2),
            ],
        ).dict(),
    ),
    (
        "/user",
        UserAdd(
            username="tester",
            nickname="测试员",
            password="123456",
            rids=[
                RoleActive(rid=2, status=5),
            ],
        ).dict(),
    ),
    # 创建菜单
    # 目录
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
    # 组件
    (
        "/menu",
        MenuIn(  # id 3
            name="用户管理",
            meta={"icon": "TeamOutlined"},
            path="/system/user",
            type=1,
            component="/system/user/user.vue",
            pid=1,
            identifier=None,
            api="/user",
            method="GET",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(  # id 4
            name="角色管理",
            meta={"icon": "UserOutlined"},
            path="/system/role",
            type=1,
            component="/system/role/role.vue",
            pid=1,
            identifier=None,
            api="/role",
            method="GET",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(  # id 5
            name="菜单管理",
            meta={"icon": "MenuOutlined"},
            path="/system/menu",
            type=1,
            component="/system/menu/menu.vue",
            pid=1,
            identifier=None,
            api="/menu",
            method="GET",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(  # id 6
            name="关于",
            meta={"icon": "DashboardOutlined"},
            path="/setting/about",
            type=1,
            component="/setting/about/about.vue",
            pid=2,
            identifier=None,
            api="/about",
            method="GET",
        ).dict(),
    ),
    # 按钮
    (
        "/menu",
        MenuIn(
            name="用户新增",
            meta={"icon": "Add"},
            path=None,
            type=2,
            component=None,
            pid=3,
            identifier="user:create",
            api="/user",
            method="POST",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="用户删除",
            meta={"icon": "Delete"},
            path=None,
            type=2,
            component=None,
            pid=3,
            identifier="user:delete",
            api="/user/{pk}",
            method="DELETE",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="用户更新",
            meta={"icon": "Update"},
            path=None,
            type=2,
            component=None,
            pid=3,
            identifier="user:update",
            api="/user/{pk}",
            method="PUT",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="用户详情",
            meta={"icon": "Info"},
            path=None,
            type=2,
            component=None,
            pid=3,
            identifier="user:get",
            api="/user/{pk}",
            method="GET",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="用户查询",
            meta={"icon": "Search"},
            path=None,
            type=2,
            component=None,
            pid=3,
            identifier="user:query",
            api="/user/query",
            method="POST",
        ).dict(),
    ),
    # 角色管理
    (
        "/menu",
        MenuIn(
            name="角色新增",
            meta={"icon": "Add"},
            path=None,
            type=2,
            component=None,
            pid=4,
            identifier="role:create",
            api="/role",
            method="POST",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="角色删除",
            meta={"icon": "Delete"},
            path=None,
            type=2,
            component=None,
            pid=4,
            identifier="role:delete",
            api="/role/{pk}",
            method="DELETE",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="查询角色拥有权限",
            meta={"icon": "Delete"},
            path=None,
            type=2,
            component=None,
            pid=4,
            identifier=None,
            api="/role/{rid}/menu",
            method="GET",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="查询角色",
            meta={"icon": "Search"},
            path=None,
            type=2,
            component=None,
            pid=4,
            identifier="",
            api="/role/query",
            method="POST",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="分配权限",
            meta={"icon": "Delete"},
            path=None,
            type=2,
            component=None,
            pid=4,
            identifier="role:assign",
            api="/role/assigned/menu",
            method="POST",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="更新角色",
            meta={"icon": "Update"},
            path=None,
            type=2,
            component=None,
            pid=4,
            identifier="role:update",
            api="/role",
            method="PUT",
        ).dict(),
    ),
    # 菜单管理的权限
    (
        "/menu",
        MenuIn(
            name="新增菜单",
            meta={"icon": "Update"},
            path=None,
            type=2,
            component=None,
            pid=5,
            identifier="menu:create",
            api="/menu",
            method="POST",
        ).dict(),
    ),
    (
        "/menu",
        MenuIn(
            name="删除菜单",
            meta={"icon": "Delete"},
            path=None,
            type=2,
            component=None,
            pid=5,
            identifier="menu:delete",
            api="/menu/{pk}",
            method="DELETE",
        ).dict(),
    ),
    # 分配权限
    (
        "/role/assigned/menu",
        RoleMenuIn(rid=1, menus=[num for num in range(1, 20)]).dict(),
    ),
    ("/role/assigned/menu", RoleMenuIn(rid=2, menus=[1, 3, 7, 8, 9, 11]).dict()),
]


@pytest.mark.parametrize("path, data", params)
def test_add_data(path, data):
    res = client.post(url=base + path, json=data)
    logger.info(res.json())
    assert res.status_code == 200
