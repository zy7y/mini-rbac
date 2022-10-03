from typing import Any, Callable, get_type_hints

from fastapi import Depends, routing

from controller.common import login, websocket
from controller.menu import menu_add, menu_arr, menu_del, menu_put
from controller.role import (
    role_add,
    role_arr,
    role_del,
    role_has_menu,
    role_put,
    role_query,
)

from core.security import check_permissions


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


has_perm = {"dependencies": [Depends(check_permissions)]}
has_perm = {}

routes = [
    Route.post("/login", endpoint=login, tags=["公共"], summary="登录"),
    # 角色管理,
    Route.get("/role", endpoint=role_arr, tags=["角色管理"], summary="角色列表", **has_perm),
    Route.post("/role", endpoint=role_add, tags=["角色管理"], summary="角色新增", **has_perm),
    Route.delete(
        "/role/{pk}", endpoint=role_del, tags=["角色管理"], summary="角色删除", **has_perm
    ),
    Route.get(
        "/role/{rid}/menu",
        endpoint=role_has_menu,
        tags=["角色管理"],
        summary="查询角色拥有权限",
        **has_perm
    ),
    Route.put(
        "/role/{pk}", endpoint=role_put, tags=["角色管理"], summary="角色更新", **has_perm
    ),
    Route.post(
        "/role/query", endpoint=role_query, tags=["角色管理"], summary="角色条件查询", **has_perm
    ),
    # 菜单新增
    Route.get("/menu", endpoint=menu_arr, tags=["菜单管理"], summary="菜单列表", **has_perm),
    Route.post("/menu", endpoint=menu_add, tags=["菜单管理"], summary="菜单新增", **has_perm),
    Route.delete(
        "/menu/{pk}", endpoint=menu_del, tags=["菜单管理"], summary="菜单删除", **has_perm
    ),
    Route.put(
        "/menu/{pk}", endpoint=menu_put, tags=["菜单管理"], summary="菜单更新", **has_perm
    ),
    routing.APIWebSocketRoute("/ws", endpoint=websocket),
]

__all__ = [routes]
