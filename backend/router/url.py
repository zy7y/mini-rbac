from typing import Any, Callable, get_type_hints

from fastapi import routing

from controller.common import login
from controller.menu import menu_add
from controller.role import role_add, role_has_menu
from controller.user import create_user, user_arr, user_info, user_list


class Route(routing.APIRoute):
    """
    https://github.com/tiangolo/fastapi/issues/620
    Django挂载视图方法
    def index() -> User:
        pass
    Route("/", endpoint=index)
    """

    def __init__(
        self,
        path: str,
        endpoint: Callable[..., Any],
        tags: list[str],
        summary: str,
        **kwargs: Any
    ):
        if kwargs.get("response_model") is None:
            kwargs["response_model"] = get_type_hints(endpoint).get("return")
        super(Route, self).__init__(
            path=path, endpoint=endpoint, tags=tags, summary=summary, **kwargs
        )

    @classmethod
    def post(
        cls,
        path: str,
        endpoint: Callable[..., Any],
        tags: list[str],
        summary: str,
        **kwargs: Any
    ):
        return Route(
            path=path,
            endpoint=endpoint,
            methods=["POST"],
            tags=tags,
            summary=summary,
            **kwargs
        )

    @classmethod
    def get(
        cls,
        path: str,
        endpoint: Callable[..., Any],
        tags: list[str],
        summary: str,
        **kwargs: Any
    ):
        return Route(
            path=path,
            endpoint=endpoint,
            methods=["GET"],
            tags=tags,
            summary=summary,
            **kwargs
        )

    @classmethod
    def delete(
        cls,
        path: str,
        endpoint: Callable[..., Any],
        tags: list[str],
        summary: str,
        **kwargs: Any
    ):
        return Route(
            path=path,
            endpoint=endpoint,
            methods=["DELETE"],
            tags=tags,
            summary=summary,
            **kwargs
        )

    @classmethod
    def put(
        cls,
        path: str,
        endpoint: Callable[..., Any],
        tags: list[str],
        summary: str,
        **kwargs: Any
    ):
        return Route(
            path=path,
            endpoint=endpoint,
            methods=["PUT"],
            tags=tags,
            summary=summary,
            **kwargs
        )


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
