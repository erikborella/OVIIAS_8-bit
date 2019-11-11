from flask import Blueprint, render_template, request, redirect, url_for
from Forms_model import LoginForm, SingupForm

from extensions import db
from Models import User

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template("login.html", form=form, errors=form.errors)


@auth.route('/singup', methods=['GET', 'POST'])
def singup():
    form = SingupForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data

        new_user = User(username, password, email)
        
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("singup.html", form=form, errors=form.errors)