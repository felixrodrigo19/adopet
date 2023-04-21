import click
from flask import Flask

from adopet.ext import models
from adopet.ext.models.database import db


def init_app(app: Flask):
    @app.cli.command()
    def create_db():
        """ Inicia o banco """
        db.create_all()
        click.echo("DB criado com sucesso!")

    @app.cli.command()
    @click.option("--username", "-e")
    @click.option("--passwd", "-p")
    def add_user(username, passwd):
        """ Adiciona usuario """
        user = models.database.User(username=username, password=passwd)  # noqa
        db.session.add(user)
        db.session.commit()
    #
    # @app.cli.command()
    # @click.option("--email", "-e")
    # def delete_user(email):
    #     """ Deleta usuario """
    #     user = models.User(
    #         email=email
    #     )
    #     db.session.delete(user)
    #     db.session.commit()
    #
    # @app.cli.command()
    # def list_users():
    #     """ Lista todos usuarios """
    #     user = models.User.query.all()
    #     click.echo(f"{user}")
