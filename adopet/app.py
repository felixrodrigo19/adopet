from dynaconf import FlaskDynaconf
from flask import Flask

from adopet.ext.database import database, migrate
from adopet.ext.database.create_db import create_db


def init_app() -> Flask:
    app = Flask(__name__)
    FlaskDynaconf(app)
    database.init_app(app=app)
    create_db(app=app, db=database.db)
    migrate.init_app(app=app)
    return app
