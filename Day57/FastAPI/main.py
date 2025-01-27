import datetime as dt

import requests
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

BLOG_URL = "https://api.npoint.io/2f1c23beb632d5f36d7d"
current_year = dt.datetime.now().year

response = requests.get(BLOG_URL)
posts = response.json()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse(
        "index.html", {"request": request, "year": current_year, "posts": posts}
    )

@app.get("/post/{number}")
async def get_post(request: Request, number: int):
    for post in posts:
        if post['id'] == number:
            return templates.TemplateResponse("post.html", {"request": request, "year": current_year, "post": post})

