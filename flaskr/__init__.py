from flask import Flask
import os


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET="dev", DATABASE=os.path.join(app.instance_path, "flaskr.sqlite")
    )

    if config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.get("/")
    def hello():
        return "Hello, World!"

    return app
