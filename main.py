from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import FileResponse
from core import experiment_router

app = FastAPI(title="bingo APIs", description="python sever powered by FastAPI")
app.add_middleware(GZipMiddleware, minimum_size=1024)


@app.get("/")
def home_page():
    """redirect you to the document page"""
    return FileResponse("data/home.html")


@app.get("/logo_rounded.png")
def get_logo():
    return FileResponse("data/logo_rounded.png")


@app.get("/default.css")
def get_css():
    return FileResponse("data/default.css")


app.include_router(experiment_router, prefix="/experiment", tags=["experiment"])
