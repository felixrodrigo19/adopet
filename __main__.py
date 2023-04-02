import os

from adopet import app

if __name__ == "__main__":
    os.environ['FLASK_DEBUG'] = "development"
    app = app.init_app()
    app.run(host='0.0.0.0')
