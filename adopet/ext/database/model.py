from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()


def get_update_date(column: str) -> Column:
    if column == "create_at":
        return Column("create_at", Date, default=datetime.utcnow())
    return Column("updated_at", Date, default=datetime.utcnow(), onupdate=datetime.utcnow())


class User(UserMixin, Model):
    id_user = Column("id_user", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String(35), unique=True, nullable=False)

    password = Column("password", String(35), nullable=False)
    created_at = get_update_date(column="created_at")
    updated_at = get_update_date(column="updated_at")

    def __repr__(self):
        return self.username

    def is_active(self):
        return self.is_active

    def is_authenticated(self):
        return self.is_authenticated


class State(Model):
    id_state = Column("id_state", db.Integer, primary_key=True, autoincrement=True)
    description = Column("description", String(60), nullable=False)

    def __repr__(self):
        return self.description


class City(Model):
    id_city = Column("id_city", db.Integer, primary_key=True, autoincrement=True)
    description = Column("description", String(60), nullable=False)
    id_state = Column("id_state", Integer, ForeignKey("state.id_state"))

    state = relationship("State", foreign_keys=id_state)

    def __repr__(self):
        return self.description


class Perfil(Model):
    id_perfil = db.Column("id_perfil", db.Integer, primary_key=True, autoincrement=True)
    phone = Column("phone", String(35), nullable=False)
    image = ...
    about_me = Column("about_me", String(90))
    created_at = get_update_date(column="created_at")
    updated_at = get_update_date(column="updated_at")
    id_user = Column("id_user", Integer, ForeignKey("User.id_user"))
    id_city = Column("id_city", Integer, ForeignKey("City.id_city"))

    user = relationship("User", foreign_keys=id_user)
    city = relationship("City", foreign_keys=id_city)


def init_app(app):
    db.init_app(app)
