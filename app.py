from flask import Flask, render_template, redirect, flash
from models import connect_db, db, User
from flask_debugtoolbar import DebugToolbarExtension 

from forms import UserForm

app = Flask(__name__)


app.config['SECRET_KEY'] = 'learningAuthenticatingUserLogin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///authentication_demo_db'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app)
db.drop_all()
db.create_all()

# @app.route('/')
# def home():
#     form = UserForm()
#     return render_template("home.html", form = form)

@app.route('/tweets')
def show_tweets():
    return render_template("tweets.html")

@app.route('/register', methods = ["GET", "POST"])
def register_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.registration(username, password)
        
        db.session.add(new_user)
        db.session.commit()

        flash("Welcome! Successfully created your account")   # why does this prints multiple times

        return redirect('/tweets')
    else:
        return render_template('register.html', form = form)

@app.route('/login', methods = ["GET", "POST"])
def login_user():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)
        if user:
            return redirect('/tweets')
        else:
            form.username.errors = ["Invalid username/password"]

    return render_template('login.html', form = form)
