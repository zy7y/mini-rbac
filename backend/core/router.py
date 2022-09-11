from typing import TYPE_CHECKING, Any, Callable, get_type_hints

from fastapi import APIRouter
from fastapi.routing import APIRoute

"""
根据类型标注自动返回模型
https://github.com/tiangolo/fastapi/issues/620
"""


class Router(APIRouter):
    """
    装饰器用法
    @app.get("/")
    def index() -> User:
    """

    if not TYPE_CHECKING:

        def add_api_route(
            self, path: str, endpoint: Callable[..., Any], **kwargs: Any
        ) -> None:
            if kwargs.get("response_model") is None:
                kwargs["response_model"] = get_type_hints(endpoint).get("return")
            return super().add_api_route(path, endpoint, **kwargs)

    else:  # pragma: no cover
        pass


class Route(APIRoute):
    """
    Django挂载视图方法
    def index() -> User:
        pass
    Route("/", endpoint=index)
    """

    if not TYPE_CHECKING:

        def __init__(self, path: str, endpoint: Callable[..., Any], **kwargs: Any):
            if kwargs.get("response_model") is None:
                kwargs["response_model"] = get_type_hints(endpoint).get("return")
            super(Route, self).__init__(path=path, endpoint=endpoint, **kwargs)

    else:  # pragma: no cover
        pass
