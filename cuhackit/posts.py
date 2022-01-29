from . import app, posts_pipe
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

# @app.post('/posts')
# def create_post(
#         curr_user = fastapi.Depends(manager),
#     ):
#     print(curr_user.username)
#     return {"username": curr_user.username}

    #adding new data to the table (insert to table in SQL)
    # posts_pipe.sync(
    #     {
    #         #uuid: rand hex generation
    #         "postID": [str(uuid.uuid4())],
    #         #get current time
    #         "time": [datetime.datetime.utcnow()],
    #         #"user": user
    #
    #     }
    # )
    # return {'test': 'foo'}

# @app.post('/user')
# def create_user():
#     return
#
#
# @app.post('/post/comment')
# def create_comment():
#     return
