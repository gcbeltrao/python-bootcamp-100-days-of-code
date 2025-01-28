from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/form")
async def form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
):
    print(f"Username: {username}\nPassword: {password}")
    return templates.TemplateResponse(
        "index.html", {"request": request, "message": "Formulário enviado!"}
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app)
