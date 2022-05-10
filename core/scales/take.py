from fastapi.responses import ORJSONResponse, HTMLResponse, RedirectResponse
from fastapi import APIRouter, Request
from random import sample
from pickle import load
from rapidfuzz.process import extract, extractOne
from rapidfuzz.fuzz import partial_ratio
from cachetools.func import lfu_cache
from starlette.templating import Jinja2Templates

app = APIRouter()

scales: dict = load(open("data/scales.pkl", "rb"))
titles = list(scales)
flattened = {title: "\n".join("\n".join(div) for div in content.values())
             for title, content in scales.items()}


@app.get("/", response_model=list[str], response_class=ORJSONResponse)
async def get_titles():
    """get all the titles on the OBHRM wiki"""
    return titles


@app.get("/random/{n}", response_model=list[str], response_class=ORJSONResponse)
async def get_random(n: int) -> list[str]:
    """randomly get ``n`` titles without caching"""
    return sample(titles, n)


@app.get("/query/{text}", response_model=list[str], response_class=ORJSONResponse)
async def query_by_title(text: str, n: int = 3) -> list[str]:
    """fuzzy matching using title"""
    return [title for title, score, index in extract(text, titles, limit=n)]


@app.get("/search/{text}", response_model=list[str], response_class=ORJSONResponse)
@lfu_cache(1024)
def search_by_content(text: str, n: int = 3) -> list[str]:
    """fuzzy matching using content"""
    return [title for content, score, title in extract(
        text, flattened, limit=n, scorer=partial_ratio
    )]

