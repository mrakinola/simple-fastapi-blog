from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from .helpers.markdown import read_markdown


from app.handlers import simple_page

app = FastAPI()
template = Jinja2Templates(directory="html_templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    info = read_markdown("home.md")
    return template.TemplateResponse("page.html", {"request": request, "info": info})


app.include_router(simple_page.router)
