from cuhackit import app, posts_pipe
from meerschaum.api import manager
import meerschaum as mrsm
import uuid
import datetime
import fastapi
from typing import Dict

#allow us to connect to the sql database on the sever
conn = mrsm.get_connector("sql", "local")

#connect to endpoint /post
@app.post('/post')
def create_post(content: Dict[str, str]):
    postID = str(uuid.uuid4())
    title = content.get("title", '(No title)')
    value = content.get("value", "(No text)")
    data = {
        "postID" : [postID],
        "time": [datetime.datetime.utcnow()],
        "title": [title],
        "value": [value],
    }
    posts_pipe.sync(data)
    return data

@app.get('/posts')
def get_posts():
    '''
    Return an array of dictionaries
    '''

    query = '''
        SELECT *
        FROM data_posts
            '''

    #executes the query and returns the data table as dictionaries
    r = conn.exec(query)
    if r is None:
        return []
    return r.mappings().all()