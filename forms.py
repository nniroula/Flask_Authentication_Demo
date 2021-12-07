from flask_wtf import FlaskForm, StringField

class LoginCredentials(FlaskForm):
    username = StringField("username")
    password = StringField("password") 
