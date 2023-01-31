from flask import Blueprint, render_template, request

bp = Blueprint('searchPage', __name__)

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    return render_template("search.html", title="Search")

@bp.route('/results')
def searchResults():
    return render_template("search_results.html", title="Results")
