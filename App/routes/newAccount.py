from flask import Blueprint, render_template
bp = Blueprint('newAccount', __name__)

@bp.route('/newaccount', methods=['GET', 'POST'])
def newAccount():
    return render_template("new-account.html")