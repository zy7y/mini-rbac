from fastapi import FastAPI

from core.events import close_orm, init_orm
from core.exceptions import exception_handlers
from core.middleware import middlewares
from core.utils import load_routers

app = FastAPI(
    on_startup=[init_orm],
    on_shutdown=[close_orm],
    middleware=middlewares,
    exception_handlers=exception_handlers,
)

load_routers(app)

# uvicorn main:app --reload
