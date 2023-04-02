from dynaconf import FlaskDynaconf
from flask import Flask

from adopet.ext.database import database
from adopet.ext.database.database import create_db


def init_app() -> Flask:
    app = Flask(__name__)
    FlaskDynaconf(app)
    database.init_app(app=app)
    create_db(app=app)
    return app
