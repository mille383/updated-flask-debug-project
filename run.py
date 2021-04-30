# from app import create_app, db, cli
from app import app, db
from app.models import Post, User
# from app.blueprints.authentication.models import User

# app = create_app()
# cli.register(app)


@app.shell_context_processor
def make_shell_context():
    # ALWAYS HAVE TO RETURN A PYTHON DICTIONARY FROM CONTEXT
    return {
        'db': db,
        'Post': Post,
        'User': User
    }