from fastapi import APIRouter, WebSocket

from schemas import common as BaseSchema
from service import auth as AuthService

router = APIRouter(tags=["公共"])


LoginResult = BaseSchema.Response[BaseSchema.LoginResult]


@router.post("/login", summary="登录")
async def login(data: BaseSchema.LoginForm) -> LoginResult:
    return await AuthService.user_login(data)


@router.websocket("/ws", name="系统信息")
async def get_system_info(ws: WebSocket):
    await AuthService.system_info(ws)
