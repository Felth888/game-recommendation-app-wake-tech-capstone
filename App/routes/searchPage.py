from flask import Blueprint, render_template, request, redirect, url_for, current_app
# app = create_app()

bp = Blueprint('searchPage', __name__)

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    if request.method == "POST":
        nameInput = request.form['nameInput'] or ""
        genreInput = request.form['genreInput'] or ""
        return(redirect(url_for('/results', nameInput=nameInput, genreInput=genreInput)))
        
    return render_template("search.html", title="Search", api_key = current_app.config['IGDB_API_KEY'])

@bp.route('/results', methods=["GET", "POST"])
def searchResults():
    # print the page with the query listed
    if request.method == "POST":
        nameInput = request.args.get('nameInput') or "Test"
        genreInput = request.args.get('genreInput') or "Testset" 
    return render_template("search-results.html", nameInput=nameInput, genreInput=genreInput) 
