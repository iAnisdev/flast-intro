from flask import Flask

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