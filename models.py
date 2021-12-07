from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
# from forms import LoginCredentials


db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)

# initialize Bcrypt/instantiate the Bcrypt
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.Text, nullable = False, unique = True)
    password = db.Column(db.Text, nullable = False)

    # create a classmethods to use it with a model class to generate
    @classmethod
    def registration(cls, username, pwd):
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode('utf8')
        return cls(username = username, password = hashed_utf8)

    @classmethod 
    def authenticate(cls, username, pwd):
        u = User.query.filter_by(username = username).first()
        if u and bcrypt.check_password_hash(u.password, pwd):  # password comes from database as hashed value)
            return u
        else:
            return False  
