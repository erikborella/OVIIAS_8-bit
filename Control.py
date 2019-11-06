from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/db'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def hello():
    return render_template('login.html')
