from flask import Blueprint, render_template, request, redirect, url_for, current_app
# app = create_app()

bp = Blueprint('searchPage', __name__)

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    return render_template("search.html", title="Search", api_key = current_app.config['IGDB_API_KEY'])
    
@bp.route('/login', methods=['GET', 'POST'])
def loginPage():
    return render_template("login.html")
