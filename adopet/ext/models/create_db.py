from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_db(app: Flask, db: SQLAlchemy):
    try:
        with app.app_context():
            db.metadata.create_all(db.engine)
    except Exception as exc:  # noqa
        print(f"{exc}")
