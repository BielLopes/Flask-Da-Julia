from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class loginFrom(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    pasword = PasswordField("pasword", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")
