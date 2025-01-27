import datetime as dt

import requests
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

BLOG_URL = "https://api.npoint.io/6e1e6892bf538acc01d4"
current_year = dt.datetime.now().year
full_date = dt.datetime.now().strftime("%B %d, %Y")

response = requests.get(BLOG_URL)
posts = response.json()


@app.get("/")
async def home(request: Request):
    last_post = next(reversed(posts))
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "posts": posts,
            "year": current_year,
            "date": full_date,
            "last_post": last_post,
        },
    )


@app.get("/posts/post{number}")
def get_post(request: Request, number: int):
    for post in posts:
        if post["id"] == number:
            correct_post = post
    return templates.TemplateResponse(
        "post.html",
        {
            "request": request,
            "year": current_year,
            "year": current_year,
            "post": correct_post,
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
