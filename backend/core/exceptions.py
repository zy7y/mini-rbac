from fastapi.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse


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


exception_handlers = {HTTPException: http_exception}
