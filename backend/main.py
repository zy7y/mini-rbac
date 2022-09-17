from fastapi import FastAPI

from controller.ws import ws_app
from core.events import close_orm, init_orm
from core.exceptions import exception_handlers
from core.log import logger
from core.middleware import middlewares
from router.url import routes

app = FastAPI(
    on_startup=[init_orm],
    on_shutdown=[close_orm],
    routes=routes,
    middleware=middlewares,
    exception_handlers=exception_handlers,
)

app.mount("/", ws_app)

if __name__ == "__main__":
    import uvicorn
    from fastapi.routing import Mount

    for i in app.routes:
        if not isinstance(i, Mount):
            logger.info(
                f"{i.path}, {i.methods}, {i.__dict__.get('summary')}, {i.endpoint}"
            )

    uvicorn.run("main:app", reload=True)
