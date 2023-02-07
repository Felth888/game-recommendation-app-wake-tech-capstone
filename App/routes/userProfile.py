from flask import Blueprint, render_template
bp = Blueprint('profile', __name__)

@bp.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template("new-account.html")
    
@bp.route('/login', methods=['GET', 'POST'])
def loginPage():
    return render_template("login.html")