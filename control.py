from app import create_app
import session
from routes.auth import auth
from routes.store import store
from routes.cart import cart

app = create_app()

app.register_blueprint(auth)
app.register_blueprint(store)
app.register_blueprint(cart)