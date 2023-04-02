from datetime import datetime

from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from sqlalchemy import Column, Integer, String, Date, ForeignKey, create_engine, text
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

    def __repr__(self) -> str:
        return f"{self.username}"

    def is_active(self):
        return self.is_active

    def is_authenticated(self):
        return self.is_authenticated


class State(Model):
    id_state = Column("id_state", Integer, primary_key=True, autoincrement=True)
    description = Column("description", String(60), nullable=False)

    def __repr__(self) -> str:
        return f"{self.description}"


class City(Model):
    id_city = Column("id_city", Integer, primary_key=True, autoincrement=True)
    description = Column("description", String(60), nullable=False)
    id_state = Column("id_state", Integer, ForeignKey("state.id_state"))

    state = relationship("State", foreign_keys=id_state)

    def __repr__(self) -> str:
        return f"{self.description}"


class Perfil(Model):
    id_perfil = db.Column("id_perfil", Integer, primary_key=True, autoincrement=True)
    phone = Column("phone", String(35), nullable=False)
    image = ...
    about_me = Column("about_me", String(90))
    created_at = get_update_date(column="created_at")
    updated_at = get_update_date(column="updated_at")
    id_user = Column("id_user", Integer, ForeignKey("User.id_user"))
    id_city = Column("id_city", Integer, ForeignKey("City.id_city"))

    user = relationship("User", foreign_keys=id_user)
    city = relationship("City", foreign_keys=id_city)

    def __repr__(self) -> str:
        return self.user


class Pet(Model):
    id_pet = Column("id_pet", Integer, primary_key=True, autoincrement=True)
    age = Column("age", String(16), nullable=False)
    description = Column("description", String(120), nullable=False)
    id_location = Column("id_location", Integer, ForeignKey("City.id_city"))
    id_responsible = Column("id_responsible", Integer, ForeignKey("User.id_user"))
    created_at = get_update_date(column="created_at")
    updated_at = get_update_date(column="updated_at")
    name = Column("name", String(60), nullable=False)

    location = relationship("City", foreign_keys=id_location)
    user = relationship("User", foreign_keys=id_responsible)

    def __repr__(self) -> str:
        return f"{self.name}"


class Contact(Model):
    id_contact = Column("id_contact", Integer, primary_key=True, autoincrement=True)
    e_mail = Column("e-mail", String(120), nullable=False)
    message = Column("message", String(300), nullable=False)
    created_at = get_update_date(column="created_at")
    updated_at = get_update_date(column="updated_at")
    id_perfil = Column("id_perfil", Integer, ForeignKey("Perfil.id_perfil"))
    id_pet = Column("id_pet", Integer, ForeignKey("Pet.id_pet"))

    perfil = relationship("Perfil", foreign_keys=id_perfil)
    pet = relationship("Pet", foreign_keys=id_pet)

    def __repr__(self) -> str:
        return f"{self.e_mail} - {self.perfil}"


def init_app(app):
    db.init_app(app)


def create_db(app: Flask):
    try:
        with app.app_context():
            db.init_app(app)
            db.create_all()

    except Exception as exc:  # noqa
        print("Database exists!\n"
              f"{exc}")
