from app import create_app
import session
from routes.auth import auth

app = create_app()

app.register_blueprint(auth)

@app.route('/')
def index():
    return str(session.get())
