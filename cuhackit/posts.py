from cuhackit import app, posts_pipe
from meerschaum.api import manager
import meerschaum as mrsm
import uuid
import datetime
import fastapi

#allow us to connect to the sql database on the sever
conn = mrsm.get_connector("sql", "local")

#connect to endpoint /post
@app.post('/post')
def create_post():
    postID = str(uuid.uuid4())
    posts_pipe.sync(
        {
            "postID" : [postID],
            "time": [datetime.datetime.utcnow()],
        }
    )
    return {
        "postID": postID,
    }

@app.get('/post')
def get_posts():

    '''
    Return an array of dictionaries
    '''

    query = '''
        SELECT *
        FROM data_posts
            '''

    #executes the query and returns the data table as dictionaries
    return conn.exec(query).mappings().all()
