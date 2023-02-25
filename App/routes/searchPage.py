from flask import Blueprint, render_template, request, redirect, url_for, current_app, json
bp = Blueprint('searchPage', __name__)
from ..models.userModels import User

@bp.route('/', methods=['GET', 'POST'])
def searchPage():
    return render_template("search.html", title="Search", api_key = current_app.config['IGDB_API_KEY'])
    
@bp.route('/add_to_library', methods=['POST'])
def add_to_library():
    # A JSON array isnt really needed to return, a string could be used
    # But a JSON array gives better control for multiple pieces of data
    adding = False
    if request.form['adding'] == "true":
        adding = True
    returnArr = {'id':request.form['id'], 'added':adding}
    return returnArr

@bp.route('/add_to_wishlist', methods=['POST'])
def add_to_wishlist():
    returnArr = {'id':request.form['id']}
    return returnArr

@bp.route('/update_library', methods=['POST'])
def update_library():
    returnArr = {'id':request.form['id']}
    return returnArr