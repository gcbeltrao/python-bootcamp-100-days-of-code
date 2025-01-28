import os
import smtplib

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

static_url = app.url_path_for("static", path="")


@app.get("/")
async def get_all_posts(request: Request):

    return templates.TemplateResponse(
        "index.html", {"request": request, "all_posts": posts, "static_url": static_url}
    )


@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse(
        "about.html", {"request": request, "static_url": static_url}
    )


@app.get("/contact")
async def get_contact(request: Request):
    return templates.TemplateResponse(
        "contact.html", {"request": request, "static_url": static_url}
    )


@app.post("/contact")
async def post_contact(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    message: str = Form(...),
):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:

        load_dotenv()
        MY_EMAIL = os.getenv("MY_EMAIL")
        PASSWORD = os.getenv("PASSWORD")

        subject = "Contact me!"
        body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        msg = f"Subject:{subject}\n\n{body}"

        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=msg.encode("utf-8")
        )
    return templates.TemplateResponse(
        "contact.html", {"request": request, "msg_sent": True, "static_url": static_url}
    )


@app.get("/post/{index}")
async def show_post(request: Request, index: int):
    requested_post = next((post for post in posts if post["id"] == index), None)
    return templates.TemplateResponse(
        "post.html",
        {"request": request, "post": requested_post, "static_url": static_url},
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
