from fastapi.exceptions import HTTPException


class TokenAuthFailure(HTTPException):
    status_code = 401
    detail = "认证失败"
