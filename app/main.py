from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

template = Jinja2Templates(directory="html-templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request)  -> template.TemplateResponse:
    info = {"page": "Home page"}
    return template.TemplateResponse("page.html", {"request": request, "info": info})


@app.get("/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str)  -> template.TemplateResponse:
    info = {"page": page_name}
    return template.TemplateResponse("page.html", {"request": request, "info": info})
