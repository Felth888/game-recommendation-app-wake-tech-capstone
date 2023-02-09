from flask import Blueprint, render_template
bp = Blueprint('profile', __name__)

@bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template("new-account.html")

