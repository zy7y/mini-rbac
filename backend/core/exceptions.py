from fastapi.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from core.log import logger


class TokenAuthFailure(HTTPException):
    pass


class PermissionsError(HTTPException):
    pass


async def http_exception(request: Request, exc: HTTPException):
    return JSONResponse(
        {"msg": exc.detail, "code": exc.status_code, "data": None},
        status_code=exc.status_code,
        headers=exc.headers,
    )


async def global_exception(request: Request, exc):
    if hasattr(request.state, "request_id"):
        request_id = request.state.request_id
    else:
        request_id = None
        logger.info("request_id 获取失败 请确认对应APIRouter使用了route_class=LogRoute ")
    logger.exception(f"{request_id} Exception Log: {exc}")
    return JSONResponse({
        "msg": str(exc),
        "code": 500,
        "data": None
    })


exception_handlers = {Exception: global_exception, HTTPException: http_exception}
