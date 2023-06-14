import time
import uuid
from typing import Callable

from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.routing import APIRoute
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from core.log import logger


# fix： 中间件没法获取到request 请求体数据 响应体
class CustomRequestLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.info(
            f"Client: {request.client} Method: {request.method}  "
            f"Path: {request.url} Headers: {request.headers}"
        )
        # python-multipart  == await request.form()
        response = await call_next(request)
        return response


class LogRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            request_id = str(uuid.uuid4())
            request.state.request_id = request_id
            logger.info(f"{request_id} Request Log {request.client} {request.method}"
                        f" {request.url} {request.headers}\n {await request.body()}")
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            logger.info(f"{request_id} Response Log {duration}s {response.headers}\n"
                        f" {response.body.decode('utf-8')}")
            return response

        return custom_route_handler


middlewares = [
    # Middleware(CustomRequestLogMiddleware),
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
]
