from .take import *
from starlette.templating import Jinja2Templates


@app.get("/html/{title}", response_class=HTMLResponse)
async def get_scale_content(request: Request, title: str):
    if (scale := scales.get(title)) is not None:
        return Jinja2Templates("./data").TemplateResponse(
            "scale_templates.html",
            {
                "request": request,
                "title": title,
                "scale": scale
            }
        )
    else:
        return RedirectResponse(f"/scales/html/{extractOne(title, titles)[0]}")


@app.get("/html", response_class=HTMLResponse)
async def page_searching():
    return open("./data/searching.html", encoding="utf-8").read()


@app.get("/{title}", response_model=dict[str, list[str]], response_class=ORJSONResponse)
async def get_scale_content(title: str) -> dict[str, list[str]]:
    """get the content of given title (best match)"""
    # key, score, index = extractOne(title, titles)
    return scales.get(title, None) or RedirectResponse(f"/scales/{extractOne(title, titles)[0]}")
