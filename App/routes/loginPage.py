from flask import Blueprint
bp = Blueprint('loginPage', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def loginPage():
    pass