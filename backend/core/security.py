from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from core.exceptions import PermissionsError, TokenAuthFailure
from dbhelper.menu import get_apis
from dbhelper.user import get_user, get_user_info
from models import UserModel

# JWT
SECRET_KEY = "lLNiBWPGiEmCLLR9kRGidgLY7Ac1rpSWwfGzTJpTmCU"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
bearer = HTTPBearer()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码 vs hash密码
    :param plain_password: 明文密码
    :param hashed_password: hash密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    加密明文
    :param password: 明文密码
    :return:
    """
    return pwd_context.hash(password)


def generate_token(username: str, expires_delta: Optional[timedelta] = None):
    """生成token"""
    to_encode = {"sub": username}.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update(dict(exp=expire))
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def check_token(security: HTTPAuthorizationCredentials = Depends(bearer)):
    """检查用户token"""
    token = security.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        return await get_user({"username": username})
    except JWTError:
        raise TokenAuthFailure(403, "认证失败")


async def check_permissions(request: Request, user: UserModel = Depends(check_token)):
    """检查接口权限"""
    # 查询当前激活角色
    result = await get_user_info(user)
    active_rid = result["roles"][0]["id"]

    # 白名单 登录用户信息， 登录用户菜单信息
    whitelist = [(f"/user/{user.id}", "GET"), (f"/role/{active_rid}/menu", "GET")] + \
        [(f"/user/role/{rid['id']}", "PUT") for rid in result['roles']]

    # 白名单 登录用户信息， 登录用户菜单信息
    if (request.url.path, request.method) in whitelist:
        return user

    api = request.url.path
    for k, v in request.path_params.items():
        api = api.replace(v, "{%s}" % k)

    # 2. 登录之后查一次 后面去结果查 todo 更新权限时需要更新 , 最好结果放redis
    cache_key = f"{user.username}_{active_rid}"
    # 缓存到fastapi 应用实例中
    if not hasattr(request.app.state, cache_key):
        setattr(request.app.state, cache_key, await get_apis(active_rid))
    if {"api": api, "method": request.method} not in getattr(
        request.app.state, cache_key
    ):
        raise PermissionsError(403, detail="无权访问")
