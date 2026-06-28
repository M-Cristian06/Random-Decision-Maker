import random 
import json 
from fastapi import FastAPI, Request, Form 
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated

# Call fastapi app 
app = FastAPI()

app.mount("/static",StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# write json file 
def create_file(choices_data=None, just_name=False):
    file_name = f"data.json"
    if just_name:
        return file_name

    json_data = json.dumps(choices_data, indent=4)
    try:
        with open(file_name, 'w') as f:
            f.write(json_data)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file")
    return file_name

# read json file 
def load_file():
    file_name = create_file(just_name=True)
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file")
    return data


# select random choice
def random_choice():
    data = load_file()
    random_c = random.choice(data)
    return random_c
    


# Main page 
@app.get("/")
def choice_ui(request: Request):
    data = load_file()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "choices": data, "random_choice": random_choice()}
    )


# ADD CHOICES FORM 
@app.get("/add_choices/")
def choice_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="choices_form.html"
    )

@app.post("/process/")
async def process_choices(choice1: Annotated[str, Form()], choice2: Annotated[str, Form()], choice3: Annotated[str, Form()], choice4: Annotated[str, Form()], choice5: Annotated[str, Form()], choice6: Annotated[str, Form()], choice7: Annotated[str, Form()]):
    print(choice1, choice2, choice3)
    data_r = [
        choice1,
        choice2,
        choice3,
        choice4,
        choice5,
        choice6,
        choice7
        ]
    create_file(data_r)
    return RedirectResponse(url="/", status_code=303)