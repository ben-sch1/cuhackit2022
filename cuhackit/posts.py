from . import app, posts_pipe, enforce_login
from meerschaum.api import manager
import meerschaum as mrsm
import uuid
import datetime
import fastapi

#allow us to connect to the sql database on the sever
conn = mrsm.get_connector("sql", "local")

@app.get('/posts')
def get_posts():
    return {'test': 'foo'}

@app.post('/posts')
def create_post(username: str):
    enforce_login(username)
    return {"username": username}

    #adding new data to the table (insert to table in SQL)
    posts_pipe.sync(
        {
            #uuid: rand hex generation
            "postID": [str(uuid.uuid4())],
            #get current time
            "time": [datetime.datetime.utcnow()],
            "user": user

        }
    )
    return {'test': 'foo'}
