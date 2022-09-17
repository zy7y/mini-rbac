import asyncio

from starlette.websockets import WebSocket

from core.security import generate_token, verify_password
from core.utils import get_system_info
from dbhelper.user import get_user
from schemas import LoginForm, LoginResult, Response


async def login(auth_data: LoginForm) -> Response[LoginResult]:
    user_obj = await get_user({"username": auth_data.username, "status__not": 9})
    if user_obj:
        if verify_password(auth_data.password, user_obj.password):
            return Response(
                data=LoginResult(
                    id=user_obj.id, token=generate_token(auth_data.username)
                )
            )
    return Response(code=400, msg="账号或密码错误")


async def websocket(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            await asyncio.sleep(1)
            await ws.send_json(get_system_info())
    except Exception as e:
        print("断开了链接", e)
        await ws.close()
