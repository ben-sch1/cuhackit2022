### ~/.config/meerschaum/plugins/example.py

from meerschaum.plugins import api_plugin

app = None

@api_plugin
def init_plugin(_app):
    """
    This function is executed immediately after the `app` is initialized.
    """
    global app
    app = _app
    from .posts import get_posts

    @app.get('/my/new/path')
    def new_path():
        return {'message': 'Hello, World!'}


