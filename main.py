from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.middleware.gzip import GZipMiddleware
from functools import cache
from fastapi import FastAPI
from os.path import isfile
from core import *

app = FastAPI(title="bingo APIs", description="python sever powered by FastAPI")
app.add_middleware(GZipMiddleware, minimum_size=1024)

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(experiment_router, prefix="/experiments", tags=["experiments"])
app.include_router(scale_router, prefix="/scales", tags=["scales"])
app.include_router(font_router, prefix="/fonts", tags=["fonts"])


@app.get("/", name="home_page")
@cache
def home_page():
    return FileResponse("./data/home.html")


class debugger:
    from loguru import logger
    debug = logger.debug
    info = logger.info
    warning = logger.warning
    error = logger.error
    critical = logger.critical

    @staticmethod
    @app.get("/refresh")
    def git_pull():
        from fastapi.responses import RedirectResponse
        from os import system
        debugger.info(system("git pull"))
        return RedirectResponse("/")

    @staticmethod
    @app.get("/debug/users", tags=["debug"])
    async def inspect_all_users():
        from core.users import User
        debugger.debug(f"{list(User.users.dict) = }")
        debugger.debug(f"{list(User.users.memo.keys()) = }")
        return list(User.users.dict.items())


@app.get("/{filepath:path}")
def get_static_assets(filepath: str):
    path = f"./data/{filepath}"
    return FileResponse(path) if isfile(path) else \
        PlainTextResponse(f"{path!r} does not exists!", 404)
