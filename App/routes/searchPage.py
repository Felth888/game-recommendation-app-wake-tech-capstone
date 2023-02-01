from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('searchPage', __name__)

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    if request.method == "POST":
        searchInput = request.form['searchInput']
        return(redirect(url_for('searchPage.searchResults', searchInput=searchInput)))
        
    return render_template("search.html", title="Search")

@bp.route('/results', methods=["GET", "POST"])
def searchResults():
    # print the page with the query listed
    if request.method == "GET":
        searchInput = request.args.get('searchInput')
        print(searchInput)
    return render_template("search-results.html", searchInput=searchInput)
