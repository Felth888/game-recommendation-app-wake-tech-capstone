from flask import Blueprint, render_template

bp = Blueprint('searchPage', __name__)

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    return render_template("search.html", title="Search")