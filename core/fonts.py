from fastapi import APIRouter
from starlette.staticfiles import StaticFiles

app = APIRouter()

app.mount("/", StaticFiles(directory="./data/fonts"), name="fonts")
