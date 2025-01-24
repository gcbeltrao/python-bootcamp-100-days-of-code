from random import randint

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

random_number = randint(0, 9)


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Pagina inicial",
            "message": "Guess a number between 0 and 9",
        },
    )


@app.get("/{number}")
def render_image(number: int, request: Request):
    if number == random_number:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "title": "Treasure",
                "message": "You found me!",
                "img_url": "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif",
                "color": "green",
            },
        )
    if number < random_number:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "title": "Try again!",
                "message": "Too low, try again!",
                "img_url": "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif",
                "color": "red",
            },
        )
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Try again!",
            "message": "Too high, try again!",
            "img_url": "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif",
            "color": "purple",
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
