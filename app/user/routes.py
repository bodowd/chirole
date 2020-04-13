from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db, login_manager
from app.models import User, credentials
from app.user.forms import LoginForm

user = Blueprint('user', __name__)


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    if username not in credentials:
        return

    user = User()
    user.id = email

    user.is_authenticated = request.form['password'] == credentials['password']
    return user


@user.route('/login', methods=['GET', 'POST'])
def login():
    # if logged in already just go to home page
    if current_user.is_authenticated:
        return render_template('logged_in.html')
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == credentials['username'] and form.password.data == credentials['password']:
            user = User()
            user.id = form.username.data
            login_user(user, remember=form.remember.data)
            # return the user, after they log in, to the page they were trying to get to but weren't logged in
            next_page = request.args.get('next')
            return redirect(url_for('main.home'))
        else:
            # danger is bootstrap class
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@user.route('/logout')
def logout():
    logout_user()
    flash('You have logged out.', 'success')
    return redirect(url_for('main.home'))
