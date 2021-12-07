from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired


class UserForm(FlaskForm):
    username = StringField("username", validators= [InputRequired()])
    password = PasswordField("password", validators= [InputRequired()]) 
