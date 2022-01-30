from typing import Optional
from fastapi import Cookie, FastAPI
import pathlib

#Package Root Directory is the root folder (cuhackit)
# / concats the new folder onto the previous dir ^
PACKAGE_ROOT_DIR = pathlib.Path(__file__).parent
IMAGES_DIR = PACKAGE_ROOT_DIR / 'images'
TEMPLATES_DIR = PACKAGE_ROOT_DIR / 'templates'
STATIC_DIR = PACKAGE_ROOT_DIR / 'static'

app = FastAPI()

#the database we are working with
INSTANCE_LABEL = "sql:local"

import meerschaum as mrsm

# a pipe is a table with a data/time access
#this is the pipe for posts
posts_pipe = mrsm.Pipe(
    "data", "posts", instance = INSTANCE_LABEL,
    #columns to create in database that will be used in the website
    columns = {"datetime": "time", "id": "postID"}
)

comments_pipe = mrsm.Pipe(
    "data", "comments", instance = INSTANCE_LABEL,
    #columns to create in database that will be used in the website
    columns = {"datetime": "time", "id": "commentID"}
)


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app.mount("/images", StaticFiles(directory=str(IMAGES_DIR)), name="images")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,})

@app.get("/forums", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("forums.html", {"request": request,})


import cuhackit.comment
import cuhackit.posts
