import asyncio

from fastapi import APIRouter
from starlette.websockets import WebSocket
from websockets.exceptions import WebSocketException

from core.security import generate_token, verify_password
from core.utils import get_system_info
from dbhelper.user import get_user
from schemas import LoginForm, LoginResult, Response

router = APIRouter(tags=["公共"])


@router.post("/login", summary="登录", response_model=Response[LoginResult])
async def login(auth_data: LoginForm):
    user_obj = await get_user({"username": auth_data.username, "status__not": 9})
    if user_obj:
        if verify_password(auth_data.password, user_obj.password):
            return Response(
                data=LoginResult(
                    id=user_obj.id, token=generate_token(auth_data.username)
                )
            )
    return Response(code=400, msg="账号或密码错误")


@router.websocket("/ws", name="系统信息")
async def websocket(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            await asyncio.sleep(1)
            await ws.send_json(get_system_info())
    except WebSocketException:
        await ws.close()
