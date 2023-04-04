from dynaconf import FlaskDynaconf
from flask import Flask

from adopet.ext.cli import cli
from adopet.ext.models import database, migrate
from adopet.ext.models.create_db import create_db
from adopet.ext.login import login_manager


def init_app() -> Flask:
    app = Flask(__name__)
    FlaskDynaconf(app)
    database.init_app(app=app)
    migrate.init_app(app=app)
    create_db(app=app, db=database.db)
    cli.init_app(app)
    login_manager.init_app(app=app)
    return app
