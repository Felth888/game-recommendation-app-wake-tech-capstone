from flask import Blueprint, render_template, request, redirect, url_for, current_app
# app = create_app()

bp = Blueprint('searchPage', __name__)

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    if request.method == "POST":
        return(redirect(url_for('/results')))
        
    return render_template("search.html", title="Search", api_key = current_app.config['IGDB_API_KEY'])

@bp.route('/results', methods=["GET", "POST"])
def searchResults():
    # print the page with the query listed
    return render_template("search-results.html", nameInput=nameInput, genreInput=genreInput) 
