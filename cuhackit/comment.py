from . import app, comments_pipe
from typing import Dict
import meerschaum as mrsm
import uuid
import datetime

conn = mrsm.get_connector("sql","local")

@app.get('/comments')
def get_comments():
    return{'test':'foo'}

@app.post('/post/{postID}/comment')
def create_comment(postID: str, content: Dict[str, str]):
    comments_pipe.sync(
        {
            "content" : [content.get("value", "Oopsie!")],
            "commentId" : [str(uuid.uuid4())],
            "postID" : [postID],
            "time": [datetime.datetime.utcnow()],
        }
    )
