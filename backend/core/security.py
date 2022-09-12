from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from core.exceptions import TokenAuthFailure
from dbhelper.user import get_user

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
        raise TokenAuthFailure
