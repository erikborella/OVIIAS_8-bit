from flask_uploads import UploadSet, IMAGES
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

from wtforms import StringField, PasswordField, IntegerField, FloatField, validators
from wtforms.validators import DataRequired, Email

images = UploadSet('images', IMAGES)


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
    email = StringField("email", validators=[DataRequired(
        "Digite seu email"), Email("Seu email esta errado")])


class ProductForm(FlaskForm):
    name = StringField(
        "name", validators=[DataRequired("Digite o nome do produto")])
    description = StringField("description", validators=[
                              DataRequired("Digite a descrição do produto")])
    price = FloatField("price", validators=[
                       DataRequired("Digite o preço do produto")])
    stock = IntegerField("stock", validators=[
                         DataRequired("Digite o estoque do produto")])
    image = FileField("image", validators=[FileRequired("Envie uma imagem")])

    admin_password = PasswordField("admin_password", validators=[
                                   DataRequired("Digite a senha de administrador"), 
                                   FileAllowed(images, "Apenas imagens")])
