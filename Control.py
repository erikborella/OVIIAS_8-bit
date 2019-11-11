from app import create_app
import session
from routes.auth import auth
from routes.store import store

app = create_app()

app.register_blueprint(auth)
app.register_blueprint(store)

@app.route('/')
def index():
    return str(session.get())
