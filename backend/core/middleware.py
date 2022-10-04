from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from core.log import logger


class CustomRequestLogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logger.info(
            f"Client: {request.client} Method: {request.method}  "
            f"Path: {request.url} Headers: {request.headers}"
        )
        # python-multipart  == await request.form()
        response = await call_next(request)
        return response


middlewares = [
    Middleware(CustomRequestLogMiddleware),
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),
]
