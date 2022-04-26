from fastapi.responses import FileResponse, PlainTextResponse
from fastapi.middleware.gzip import GZipMiddleware
from functools import cache
from fastapi import FastAPI
from os.path import isfile
from core import *

app = FastAPI(title="bingo APIs", description="python sever powered by FastAPI")
app.add_middleware(GZipMiddleware, minimum_size=1024)

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(scale_router, prefix="/scales", tags=["scales"])
app.include_router(experiment_router, prefix="/experiments", tags=["experiments"])
app.include_router(font_router, prefix="/fonts", tags=["fonts"])


@app.get("/", name="home_page")
@cache
def home_page():
    return FileResponse("./data/home.html")


@app.get("/{filepath:path}")
def get_static_resources(filepath: str):
    path = f"./data/{filepath}"
    return FileResponse(path) if isfile(path) else \
        PlainTextResponse(f"{path!r} does not exists!", 404)
