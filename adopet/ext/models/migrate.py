from flask_migrate import Migrate

from adopet.ext.models import database

migrate = Migrate()


def init_app(app):
    migrate.init_app(app=app, db=database)
