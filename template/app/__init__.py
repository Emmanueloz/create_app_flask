from flask import Flask
from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/")
    def index():
        return "<h1>Hello World in Flask</h1>"

    return app
