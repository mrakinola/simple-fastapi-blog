from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from ..helpers.markdown import read_markdown

router = APIRouter()

template = Jinja2Templates(directory="html_templates")

router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/{page_name}", response_class=HTMLResponse)
async def generic_page(request: Request, page_name: str):
    info = read_markdown(page_name + ".md")
    return template.TemplateResponse("page.html", {"request": request, "info": info})
