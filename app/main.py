from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

template = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request) -> template.TemplateResponse:
    info = {"page": "Home Page"}
    return template.TemplateResponse("page.html", {"request": request, "info": info})
