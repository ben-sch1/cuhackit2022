### ~/.config/meerschaum/plugins/example.py

from meerschaum.plugins import api_plugin
from typing import Optional
from fastapi import Cookie, FastAPI

app = None

#ensure that the username of a post or comment is not blank
def enforce_login(username):
    """
    Make sure the username cookie is set.
    """
    if username is None:
        raise Exception("Not authenticated!")

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

@api_plugin
def init_plugin(_app):
    """
    This function is executed immediately after the `app` is initialized.
    """
    global app
    app = _app
    from .comment import create_comment