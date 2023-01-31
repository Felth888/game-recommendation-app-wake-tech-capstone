from flask import Blueprint
bp = Blueprint('newAccount', __name__)

@bp.route('/newaccount', methods=['GET', 'POST'])
def newAccount():
    pass