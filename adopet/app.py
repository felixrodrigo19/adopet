from flask import Flask

from adopet.ext.database import model


def init_app() -> Flask:
    app = Flask(__name__)
    database = model.init_app(app=app)

    return app
