from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('searchPage', __name__)

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    if request.method == "POST":
        name = request.form['name']
        print(name)
        return(redirect(url_for('searchResults')))
        
    return render_template("search.html", title="Search")

@bp.route('/results', methods=["GET", "POST"])
def searchResults():
    # print the page with the query listed
    return render_template("search-results.html")
