from flask import Flask
from extensions import db, toolbar

def create_app(debug=True):
    app = Flask(__name__)
    app.debug = debug
    
    set_configurations(app)
    register_extension(app)

    return app

def set_configurations(app):
    app.secret_key = "personificação"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/db'


def register_extension(app):
    db.init_app(app)
    toolbar.init_app(app)
