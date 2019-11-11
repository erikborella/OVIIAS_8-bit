from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from routes.auth import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/db'
db = SQLAlchemy(app)

app.register_blueprint(auth)

@app.route('/')
def hello_world():
    return 'Hello World!'
