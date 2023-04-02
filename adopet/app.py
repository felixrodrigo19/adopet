from dynaconf import FlaskDynaconf
from flask import Flask

from adopet.ext.database import database


def init_app() -> Flask:
    app = Flask(__name__)
    FlaskDynaconf(app)
    database.init_app(app=app)
    return app
