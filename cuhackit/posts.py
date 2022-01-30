from . import app, posts_pipe, enforce_login
from meerschaum.api import manager
import meerschaum as mrsm
import uuid
import datetime
import fastapi

#allow us to connect to the sql database on the sever
conn = mrsm.get_connector("sql", "local")


@app.post('/post')
def create_post(postID: str):
    posts_pipe.sync(
        {
            "postID" : [str(uuid.uuid4())],
            "time": [datetime.datetime.utcnow()],
        }
    )

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

@app.post('/posts')
def create_post():

    #adding new data to the table (insert to table in SQL)
    return posts_pipe.sync(
        {
            #uuid: rand hex generation
            "postID": [str(uuid.uuid4())],
            #get current time
            "time": [datetime.datetime.utcnow()]

        }
    )
