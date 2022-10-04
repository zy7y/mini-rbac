import asyncio

from websockets.exceptions import WebSocketException

from core.dbhelper import has_user
from core.security import generate_token, verify_password
from core.utils import get_system_info


async def user_login(data):
    """用户登录"""
    user_obj = await has_user(data.username)
    if user_obj:
        if verify_password(data.password, user_obj.password):
            return dict(data=dict(id=user_obj.id, token=generate_token(data.username)))
    return dict(code=400, msg="账号或密码错误")


async def system_info(ws):
    await ws.accept()
    try:
        while True:
            await asyncio.sleep(1)
            await ws.send_json(get_system_info())
    except WebSocketException:
        await ws.close()
