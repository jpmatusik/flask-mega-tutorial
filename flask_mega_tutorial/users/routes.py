from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required, login_user, logout_user

from flask_mega_tutorial import db
from flask_mega_tutorial.models import User
from flask_mega_tutorial.users.forms import LoginForm, RegistrationForm

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('You logged in!', 'success')
            return redirect(url_for('main_bp.home'))
        flash('Login did not succeed. Verify your email/password and try again.', 'warn')
    return render_template('login.html', title='Login', form=form)


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = User.hash_password(form.password.data)
        user = User(email=form.email.data, username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Acccount successfully created!', 'success')
        return redirect(url_for('users_bp.login'))
    return render_template('register.html', title='Register', form=form)

@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are now logged out.', 'info')
    return redirect(url_for('main_bp.home'))
