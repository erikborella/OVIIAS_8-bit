from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.secret_key = "personificação"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/db'
    register_extension(app)
    return app

def register_extension(app):
    db.init_app(app)
