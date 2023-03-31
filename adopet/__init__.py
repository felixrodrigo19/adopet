from dynaconf import FlaskDynaconf


def init_app(app) -> None:
    """
    Setup config with Dynaconf
    :param app: instance of Flask
    :return: None
    """
    FlaskDynaconf(app)
