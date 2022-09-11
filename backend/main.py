from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from controller import register_routers
from core.events import close_orm, init_orm
from core.log import logger_db_client
from core.utils import menu_table

app = FastAPI(
    on_startup=[init_orm, menu_table],
    on_shutdown=[close_orm],
    docs_url=None,
    redoc_url=None,
)

register_routers(app)


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.bootcdn.net/ajax/libs/swagger-ui/4.10.3/swagger-ui.css",
    )


for i in app.routes:
    logger_db_client.debug(i.__dict__)
    logger_db_client.info(f"{i.path}, {i.methods}, {i.path_regex}")
    """
     'path_regex': re.compile('^/role/(?P<
pk>[^/]+)/menu$'), 'path_format': '/role/{pk}/menu', 
    """


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", reload=True)