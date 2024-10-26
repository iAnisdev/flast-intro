from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello():
    return "<p>Hello, World!</p>"

@app.route('/about')
def about():
    return "<p>About me</p>"


@app.route('/<name>')
def greet(name):
    return f"<p>Hello, {name}!</p>"

@app.route('/user/<int:user_id>')
def user(user_id):
    print(type(user_id))
    return f"<p>User {user_id}</p>"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'