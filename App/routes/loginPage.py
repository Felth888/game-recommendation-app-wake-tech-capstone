from flask import Blueprint, render_template, flash, redirect, url_for, request
bp = Blueprint('loginPage', __name__)
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from ..models import db
from ..models.userModels import User
from ..services.forms import LoginForm




@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('searchPage.searchPage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('loginPage.login'))
        login_user(user)
        return redirect(url_for('searchPage.searchPage'))
    return render_template('login.html', title='Log In', form=form)
    
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('searchPage.searchPage'))