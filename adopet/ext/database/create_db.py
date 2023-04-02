def create_db(app, db):
    try:
        with app.app_context():
            db.create_all()

    except Exception as exc:  # noqa
        print("Database exists!\n"
              f"{exc}")
