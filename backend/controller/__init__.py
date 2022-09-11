from fastapi import Depends, FastAPI

from core.security import check_token


def register_routers(app: FastAPI):
    from controller.common import common
    from controller.menu import menu
    from controller.role import role
    from controller.user import user

    app.include_router(router=common)
    app.include_router(
        router=user,
    )
    app.include_router(router=menu)
    app.include_router(router=role)
