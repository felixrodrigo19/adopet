from adopet import app

if __name__ == "__main__":
    app = app.init_app()
    app.run(host='0.0.0.0')
