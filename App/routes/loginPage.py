from flask import Blueprint, render_template
bp = Blueprint('loginPage', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def loginPage():
    return render_template("login.html")
    
@bp.route('/newaccount', methods=['GET', 'POST'])
def newAccountPage():
    return render_template("new-account.html")