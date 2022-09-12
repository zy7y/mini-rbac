import json

import requests as client

from schemas.menu import MenuIn
from schemas.role import RoleIn
from schemas.user import UserIn

base = "http://localhost:8000"


def test_user_add():
    url = base + "/user"
    res = client.request(
        method="post",
        url=url,
        json=UserIn(username="admin", nickname="超级管理员", password="123456").dict(),
    )
    assert res.status_code == 200
    res = client.request(
        method="post",
        url=url,
        json=UserIn(username="tester", nickname="测试员", password="123456").dict(),
    )
    assert res.status_code == 200


def test_role_add():
    url = base + "/role"
    res = client.request(
        method="post", url=url, json=RoleIn(name="super", remark="全部权限").dict()
    )
    assert res.status_code == 200
    res = client.request(
        method="post", url=url, json=RoleIn(name="user", remark="用户权限").dict()
    )
    assert res.status_code == 200


def test_menu_add():
    url = base + "/menu"
    # id 1
    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="系统管理",
            meta=json.dumps({"icon": "Group"}),
            path="/system",
            type=0,
            component=None,
            pid=0,
            identifier=None,
            api=None,
            method=None,
            regx=None,
        ).dict(),
    )

    assert res.status_code == 200
    # id 2
    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="用户管理",
            meta=json.dumps({"icon": "User"}),
            path="/system/user",
            type=1,
            component="/system/user.vue",
            pid=1,
            identifier=None,
            api="/user",
            method="{'GET'}",
            regx="^/user$",
        ).dict(),
    )
    assert res.status_code == 200
    # id 3
    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="角色管理",
            meta=json.dumps({"icon": "User"}),
            path="/system/role",
            type=1,
            component="/system/role.vue",
            pid=1,
            identifier=None,
            api="/role",
            method="{'GET'}",
            regx="^/role$",
        ).dict(),
    )

    # id 4
    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="菜单管理",
            meta=json.dumps({"icon": "Menu"}),
            path="/system/menu",
            type=1,
            component="/system/menu.vue",
            pid=1,
            identifier=None,
            api="/menu",
            method="{'GET'}",
            regx="^/menu$",
        ).dict(),
    )

    # id 5
    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="系统设置",
            meta=json.dumps({"icon": "Setting"}),
            path="/setting",
            type=0,
            component=None,
            pid=0,
            identifier=None,
            api=None,
            method=None,
            regx=None,
        ).dict(),
    )

    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="系统监控",
            meta=json.dumps({"icon": "minitor"}),
            path="/setting/minitor",
            type=0,
            component="/setting/minitor.vue",
            pid=5,
            identifier=None,
            api=None,
            method=None,
            regx=None,
        ).dict(),
    )

    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="新增用户",
            meta=json.dumps({"icon": "Add"}),
            path=None,
            type=2,
            component=None,
            pid=2,
            identifier="user:add",
            api="/user",
            method="{'POST'}",
            regx="^/user$",
        ).dict(),
    )
    assert res.status_code == 200

    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="查询用户",
            meta=json.dumps({"icon": "Select"}),
            path=None,
            type=2,
            component=None,
            pid=2,
            identifier="user:query",
            api="/user/query",
            method="{'POST'}",
            regx="^/user/query$",
        ).dict(),
    )

    res = client.request(
        method="post",
        url=url,
        json=MenuIn(
            name="角色管理",
            meta=json.dumps({"icon": "User"}),
            path="/system/role",
            type=1,
            component="/system/role.vue",
            pid=1,
            identifier=None,
            api="/role",
            method="{'GET'}",
            regx="^/role",
        ).dict(),
    )
    assert res.status_code == 200
