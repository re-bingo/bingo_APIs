from fastapi.responses import FileResponse, RedirectResponse
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.templating import Jinja2Templates
from cachetools.func import ttl_cache
from markdown2 import markdown
from functools import cache
from os.path import isfile
from datetime import date
from requests import get
from core import *

app = FastAPI(title="bingo APIs", description="python sever powered by FastAPI")
# app.add_middleware(GZipMiddleware, minimum_size=1024)
app.add_middleware(BrotliMiddleware, minimum_size=1024)
app.add_middleware(CORSMiddleware, allow_methods=["*"], allow_headers=["*"])

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(experiment_router, prefix="/experiments", tags=["experiments"])
app.include_router(scale_router, prefix="/scales", tags=["scales"])
app.include_router(font_router, prefix="/fonts", tags=["fonts"])


@ttl_cache(None, 60 * 60)
def get_cwj_readme():
    return get("https://github-readme-stats.vercel.app/api?username=hexWars&show_icons=true&bg_color=00000000").text


@cache
def get_badge():
    return get("https://img.shields.io/badge/Bingo APIs-Muspi Merol> -gray.svg?"
               "colorA=5760a2&colorB=475092&style=for-the-badge").text


@app.get("/", name="home_page")
async def home_page(request: Request):
    return Jinja2Templates("./data").TemplateResponse(
        "home.html",
        {
            "request": request,
            "readme": markdown(open("./readme.md", encoding="utf-8").read()),
            "date": f"—— today is {date.today()} ——",
            "cwj": get_cwj_readme(),
            "badge": get_badge()
        }
    )


class debugger:
    from loguru import logger
    debug = logger.debug
    info = logger.info
    warning = logger.warning
    error = logger.error
    critical = logger.critical

    @staticmethod
    @app.get("/refresh", tags=["debug"])
    def git_pull():
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
    if isfile(path):
        return FileResponse(path)
    else:
        raise HTTPException(404, f"fall back to static assets function and "
                                 f"{path!r} does not exists!")
