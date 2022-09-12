from controller.common import login
from controller.menu import menu_add
from controller.role import role_add, role_has_menu
from controller.user import create_user, user_arr, user_info, user_list
from core import Route

routes = [
    Route.post("/login", endpoint=login, tags=["公共"], summary="登录"),
    #   用户管理
    Route.post("/user", endpoint=create_user, tags=["用户管理"], summary="用户新增"),
    Route.get("/user/{pk}", endpoint=user_info, tags=["用户管理"], summary="用户信息"),
    Route.get("/user", endpoint=user_arr, tags=["用户管理"], summary="用户列表"),
    Route.post("/user/query", endpoint=user_list, tags=["用户管理"], summary="用户列表查询"),
    # 角色管理
    Route.post("/role", endpoint=role_add, tags=["角色管理"], summary="角色新增"),
    Route.get(
        "role/{rid}/menu", endpoint=role_has_menu, tags=["角色管理"], summary="查询角色拥有权限"
    ),
    # 菜单新增
    Route.post("/menu", endpoint=menu_add, tags=["菜单管理"], summary="菜单新增"),
]

__all__ = [routes]
