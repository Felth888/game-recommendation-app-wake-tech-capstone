from flask import Blueprint, render_template, request, redirect, url_for, current_app, json
from flask_login import current_user
bp = Blueprint('searchPage', __name__)
from ..models.userModels import User
from ..models.uGameModels import UserGame
from ..models.gameModels import Game
from ..models import db

from ..services.libraryUtils import getLibraryString, getWishlistString

@bp.route('/', methods=['GET', 'POST'])
def searchPage():

    # If the user is logged in, 
    if current_user.is_authenticated:
        # Load all the user's library games
        lib_id_string = getLibraryString(current_user.id)
        wish_id_string = getWishlistString(current_user.id)
        return render_template("search.html", title="Search", api_key = current_app.config['IGDB_API_KEY'], library_id_list = lib_id_string, wishlist_id_list = wish_id_string)
        
    # Non-logged in user gets the regular tempate
    return render_template("search.html", title="Search", api_key = current_app.config['IGDB_API_KEY'])
    

# Adds a game to a user's library
@bp.route('/add_to_library', methods=['POST'])
def add_to_library():

    # A JSON array isnt really needed to return, a string could be used
    # But a JSON array gives better control for multiple pieces of data
    adding = False
    if request.form['adding'] == "true":
        # Since a game is being added, first check to see if the record exists and is archived
        foundGame = UserGame.query.filter_by(user_id=current_user.id, game_id=request.form['id']).first()
        if foundGame:
            foundGame.archived = False
        # If the game doesnt exist in the user's library, add it
        else:
            newGame = UserGame(user_id=current_user.id, game_id=request.form['id'])
            db.session.add(newGame)
        adding = True
    else:
        # If we're not adding a game, its being archived. Query to get the entry then archive it
        foundGame = UserGame.query.filter_by(user_id=current_user.id, game_id=request.form['id']).first()
        foundGame.archived = True;

    # Adding or removing, commit the changes
    db.session.commit()
    # Create the return array with the game ID and whether something was added/removed
    returnArr = {'id':request.form['id'], 'added':adding}

    return returnArr


# Adds a game to a user's wishlist
@bp.route('/add_to_wishlist', methods=['POST'])
def add_to_wishlist():

    # A JSON array isnt really needed to return, a string could be used
    # But a JSON array gives better control for multiple pieces of data
    adding = False
    if request.form['adding'] == "true":
        # Since a game is being added, first check to see if the record exists and is archived
        foundGame = UserGame.query.filter_by(user_id=current_user.id, game_id=request.form['id']).first()
        if foundGame:
            foundGame.wishlist = True
        # If the game doesnt exist in the user's library, add it
        else:
            newGame = UserGame(user_id=current_user.id, game_id=request.form['id'], wishlist=True)
            db.session.add(newGame)
        adding = True
    else:
        # If we're not adding a game, its being archived. Query to get the entry then archive it
        foundGame = UserGame.query.filter_by(user_id=current_user.id, game_id=request.form['id']).first()
        foundGame.wishlist = False

    # Adding or removing, commit the changes
    db.session.commit()
    # Create the return array with the game ID and whether something was added/removed
    returnArr = {'id':request.form['id'], 'added':adding}

    return returnArr


# Checks the games database to see if this game has been added to the local database yet
@bp.route('/update_catalog', methods=['POST'])
def update_catalog():
    # Check if quering for the game results in anything coming back
    foundGame = Game.query.filter_by(id=request.form['id']).first()
    # If nothing is found, create an entry for the game and send it into the DB
    if not foundGame:
        newGame = Game(id=request.form['id'],title=request.form['title'])
        db.session.add(newGame)
        db.session.commit()
        print(str(newGame.title) + " IS BEING ADDED")

    returnArr = {'id':request.form['id']}
    return returnArr