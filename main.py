from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import RedirectResponse
from core import experiment_router

app = FastAPI(title="bingo APIs", description="python sever powered by FastAPI")
doc = RedirectResponse("/redoc")
app.add_middleware(GZipMiddleware, minimum_size=1024)


@app.get("/")
def home_page():
    """redirect you to the document page"""
    return doc


app.include_router(experiment_router, prefix="/experiment", tags=["experiment"])
