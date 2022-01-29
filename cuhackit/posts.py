from . import app

@app.get('/posts')
def get_posts():
    return {'test': 'foo'}
