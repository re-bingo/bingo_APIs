from fastapi import APIRouter
from fastapi.responses import Response

app = APIRouter()


def load_font(filename):
    return open(f"./data/fonts/{filename}", "rb").read()


regular = load_font("HarmonyOS_Sans_SC_Regular.ttf")
bold = load_font("HarmonyOS_Sans_SC_Bold.ttf")
serif = load_font("FZPingXYSK.TTF")
art = load_font("FZZuoZYXTJW-L.TTF")


@app.get("/regular")
def get_regular_font():
    return Response(regular)


@app.get("/bold")
def get_bold_font():
    return Response(bold)


@app.get("/serif")
def get_serif_font():
    return Response(serif)


@app.get("/art")
def get_art_font():
    return Response(art)
