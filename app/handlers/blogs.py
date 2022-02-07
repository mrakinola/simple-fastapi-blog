from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from ..helpers.markdown import read_markdown


router = APIRouter()

template = Jinja2Templates(directory="html_templates")

router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get("/{blogs}", response_class=HTMLResponse)
async def blog_table_of_contents(request: Request, blogs: str):
    pass


