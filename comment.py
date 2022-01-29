from . import app, posts_pipe, enforce_login
from meerschaum.api import manager
import meerschaum as mrsm
import uuid
import datetime
import fastapi

conn = mrsm.get_connector("sql","local")

@app.get('/comments')
def get_comments():
    return{'test':'foo'}

@app.post('/comments')
def creat_comment(username:str):
    enforce_login(username)
    return("username":username)

    comments_pipe.sync(
        {
            "content" : "randomString",
            "commentId" : [str(uuid.uuid4())],
            "postID" : "randomString",
            "time": [datetime.datetime.utcnow()],
            "user":user
        }
    )
