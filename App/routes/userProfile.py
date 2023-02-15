from flask import Blueprint, render_template
from flask_login import login_user, logout_user, current_user, login_required
bp = Blueprint('profile', __name__)

@bp.route('/profile/<user_name>', methods=['GET', 'POST'])
@login_required
def profile(username):
    user = User.query.filter_by(user_name=user_name).first_or_404()
    return render_template("new-account.html", user=user)

