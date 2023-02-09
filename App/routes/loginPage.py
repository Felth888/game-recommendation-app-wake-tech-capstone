from flask import Blueprint, render_template
bp = Blueprint('loginPage', __name__)
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_bcrypt import Bcrypt

login_manager = LoginManager()
bcrypt = Bcrypt()

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(user_id)


@bp.route('/login', methods=['GET', 'POST'])
def loginPage():
    return render_template("login.html")
    