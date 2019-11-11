from app import create_app
from routes.auth import auth

app = create_app()

app.register_blueprint(auth)

@app.route('/')
def index():
    return 'Hello World!'
