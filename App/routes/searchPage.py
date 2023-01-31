from flask import Blueprint
bp = Blueprint('searchPage', __name__)

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    pass