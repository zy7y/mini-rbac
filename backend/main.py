from fastapi import Depends, FastAPI
import uvicorn
from core.events import close_orm, init_orm
from core.exceptions import exception_handlers
from core.middleware import middlewares
from core.security import check_permissions
from core.utils import load_routers

app = FastAPI(
    on_startup=[init_orm],
    on_shutdown=[close_orm],
    middleware=middlewares,
    exception_handlers=exception_handlers,
)

load_routers(app, "router", no_depends="auth", depends=[Depends(check_permissions)])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
