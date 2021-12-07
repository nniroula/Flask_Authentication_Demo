from flask import Flask, render_template
from models import connect_db, db
from flask_debugtoolbar import DebugToolbarExtension 
from forms import LoginCredentials

app = Flask(__name__)
connect_db(app)
# db.create_all()

app.config['SECRET_KEY'] = 'learningAuthenticatingUserLogin'
app.config['SQLALCHEMY_DATABASE_URI'] = 'Postgresql:///authentication_demo_db'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)



@app.route('/')
def home():
    form = LoginCredentials()
    return render_template("home.html", form = form)