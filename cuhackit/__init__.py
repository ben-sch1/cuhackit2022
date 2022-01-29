### ~/.config/meerschaum/plugins/example.py

from meerschaum.plugins import api_plugin
from typing import Optional

app = None

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
posts_pipe = mrsm.Pipe(
    "data", "posts", instance = INSTANCE_LABEL,
    #columns to create in database that will be used in the website
    columns = {"datetime": "time", "id": "postID"}
)

comments_pipe = mrsm.Pipe(
    "data", "posts", instance = INSTANCE_LABEL,
    #columns to create in database that will be used in the website
    columns = {"datetime": "time", "id": "postID"}
)

@api_plugin
def init_plugin(_app):
    """
    This function is executed immediately after the `app` is initialized.
    """
    global app
    app = _app

    # from meerschaum.api._oauth2
    # from meerschaum.api.routes._login import load_user, login
    # from .posts import get_posts

    # from meerschaum.api import manager
    import fastapi

    @app.get('/bar')
    def bar(username: Optional[str] = Cookie(None)):
        enforce_login(username)
        return {'bar': 'foo'}
