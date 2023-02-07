from flask import Blueprint, render_template
bp = Blueprint('loginPage', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def loginPage():
    return render_template("login.html")