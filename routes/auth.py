from flask import Blueprint, render_template, request, redirect, url_for
from Forms_model import LoginForm, SingupForm

from extensions import db
from Models import User

import session
import hashlib

auth = Blueprint('auth', __name__)


def hash_string(string):
    sha_signature = hashlib.sha256(string.encode()).hexdigest()
    return sha_signature


def check_existent_username(username):
    users = User.query.all()
    for user in users:
        if user.username == username:
            return True


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = hash_string(form.password.data)

        user: User = User.query.filter_by(
            username=username, password=password).first()

        if user is None:
            return render_template("login.html", form=form, errors=form.errors, error="Usuario não encontrado")
        else:
            session.add(user.id)
            return redirect(url_for('store.index'))
    return render_template("login.html", form=form, errors=form.errors)


@auth.route('/singup', methods=['GET', 'POST'])
def singup():
    form = SingupForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        if (check_existent_username(username)):
            return render_template("singup.html", form=form, errors=form.errors, error="nome de usuario ja existente")
        else:
            new_user = User(username, hash_string(password), email)

            db.session.add(new_user)
            db.session.commit()
            session.add(new_user.id)

        return redirect(url_for("store.index"))

    return render_template("singup.html", form=form, errors=form.errors)


@auth.route('/singout')
def singout():
    session.remove()
    return redirect(url_for("auth.login"))
