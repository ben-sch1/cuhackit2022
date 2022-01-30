from cuhackit import app, comments_pipe
from meerschaum.api import manager
from typing import Dict
import meerschaum as mrsm
import uuid
import datetime

conn = mrsm.get_connector("sql","local")

@app.get('/post/{postID}/comments')
def get_comments(postID: str):

    '''
    Return an array of dictionaries
    '''

    #format string, insecure
    query = f'''
        SELECT *
        FROM data_comments
        WHERE "postID" = '{postID}'
        '''

    #executes the query and returns the data table as dictionaries
    return conn.exec(query).mappings().all()

@app.post('/post/{postID}/comments')
def create_comment(postID: str, content: Dict[str, str]):
    commentID = str(uuid.uuid4())
    data = {
        "content" : [content.get("value", "Oopsie!")],
        "commentID" : commentID,
        "postID" : [postID],
        "time": [datetime.datetime.utcnow()],
    }
    comments_pipe.sync(
        data 
    )
    return data