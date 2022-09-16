from fastapi import FastAPI
from fastapi.websockets import WebSocket

from core.utils import get_system_info

# websocket app
ws_app = FastAPI()


@ws_app.websocket("/ws")
async def ws_func(ws: WebSocket):
    await ws.accept()
    while True:
        await ws.send_json(get_system_info())
