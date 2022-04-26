from fastapi import APIRouter
from fastapi.responses import FileResponse

app = APIRouter()


@app.get("/regular")
def get_regular_font():
    return FileResponse("./data/fonts/HarmonyOS_Sans_SC_Regular.ttf")


@app.get("/bold")
def get_bold_font():
    return FileResponse("./data/fonts/HarmonyOS_Sans_SC_Bold.ttf")
