# from typing import Union
from fastapi import FastAPI
from app import router as AppsRoute
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()

app.include_router(AppsRoute.router)

register_tortoise(
    app,
    db_url="postgres://postgres:ainy@127.0.0.1/imageupload",
    modules={"models": ['app.models',]},
    generate_schemas=True,
    add_exception_handlers=True
)
