from flask import flash
from flask_login import LoginManager

from adopet.ext.models.database import User

login_manager: LoginManager = LoginManager()


class Login:

    @login_manager.user_loader
    def load_user(self, id_user):
        user = User.query.filter_by(id_user=id_user).first()
        if user:
            return user
        return

    @login_manager.unauthorized_handler
    def unauthorized(self):
        flash("Usuário não logado no sistema.")
        return


def init_app(app):
    login_manager.init_app(app=app)
    Login()
