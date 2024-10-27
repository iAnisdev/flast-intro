from flask import Flask
import os , uuid
from . import auth , home

def create_app(config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = str(uuid.uuid4())

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

    app.register_blueprint(auth.bp)
    app.register_blueprint(home.bp)

    return app
