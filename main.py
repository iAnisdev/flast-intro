from flask import Flask , url_for
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
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('about'))
    print(url_for('greet', name='John Doe'))
    print(url_for('user', user_id=1))
    print(url_for('show_subpath', subpath='subpath'))
    print(url_for('projects'))