from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("username", validators=[
                           DataRequired("Digite seu nome de usuario")])
    password = PasswordField("password", validators=[
                             DataRequired("Digite sua senha")])


class SingupForm(FlaskForm):
    username = StringField("username", validators=[
                           DataRequired("Digite seu nome de usuario")])
    password = PasswordField("password", validators=[
                             DataRequired("Digite sua senha")])
