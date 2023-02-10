from flask import Blueprint, render_template
bp = Blueprint('loginPage', __name__)
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

from ..models import db
from ..models.userModels import User
from ..services.forms import LoginForm




@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('Search'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('Log In'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('Search'))
    return render_template('login.html', title='Log In', form=form)
    
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Search'))