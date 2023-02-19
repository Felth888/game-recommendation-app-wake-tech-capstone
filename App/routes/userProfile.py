from flask import Blueprint, render_template
from flask_login import login_user, logout_user, current_user, login_required
bp = Blueprint('userProfile', __name__)
from ..models.userModels import User

@bp.route('/profile/<user_name>', methods=['GET', 'POST'])
@login_required
def profile(user_name):
    user = User.query.filter_by(user_name=user_name).first_or_404()
    return render_template("user-profile.html", user=user)

