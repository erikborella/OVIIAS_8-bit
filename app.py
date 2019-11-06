from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/login')
def hello():
    return render_template('login.html')

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host = "0.0.0.0")
=======
    app.run(host="0.0.0.0")
>>>>>>> e4816516cadeeb6d3233b118c1e4606c9f797e77
