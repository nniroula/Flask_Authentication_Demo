from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class USer(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.Text, nullable = False, unique = True)
    password = db.Column(db.Text, nullable = False)


def connect_db(app):
    db.app = app
    db.init_app(app)

db.drop_all()
db.create_all()
