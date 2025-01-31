from fastapi import Depends, FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr, Field, ValidationError

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class LoginForm(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=30)
    
    @classmethod
    def as_form(cls, email: str = Form(...), password: str = Form(...)):
        return cls(email=email, password=password)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
def get_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def post_login(request: Request, email: str = Form(...), password: str = Form(...)):
    try:
        form_data = LoginForm(email=email, password=password)
    except ValidationError:
        return templates.TemplateResponse("login.html", {"request": request, "message": "Email inválido, tente novamente."})
    if form_data.email == "admin@email.com" and form_data.password == "12345678":
        return templates.TemplateResponse("success.html", {"request": request})
    return templates.TemplateResponse("denied.html", {"request": request})

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)