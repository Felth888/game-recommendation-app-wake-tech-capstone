from flask import Blueprint, render_template, request, redirect, url_for, current_app, json
import requests
from datetime import datetime
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
            foundGame.wishlist = None # Games added to library are removed from the wishlist
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
    foundGame = UserGame.query.filter_by(user_id=current_user.id, game_id=request.form['id']).first()
    if request.form['adding'] == "true":
        # Since a game is being added, first check to see if the record exists and is archived
        if foundGame:
            foundGame.wishlist = True
        # If the game doesnt exist in the user's library, add it
        else:
            newGame = UserGame(user_id=current_user.id, game_id=request.form['id'], wishlist=True)
            db.session.add(newGame)
        adding = True
    else:
        # If we're not adding a game, its being archived. Query to get the entry then archive it
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

        # Get the information from the existing form that was submitted
        id = request.form['id']
        title = request.form['title']

        # Make a POST request to get the data for the new title from IGDB
        url = "https://5jmkis1ked.execute-api.us-west-2.amazonaws.com/production/v4/games"

        payload = "fields cover.image_id, category, release_dates.date, genres.name, themes.name, game_modes.name, involved_companies.company.name, involved_companies.developer;"
        payload += "where id=" + str(id) + "; limit 1;"
        headers = {"x-api-key": current_app.config['IGDB_API_KEY'], 'Content-Type': 'application/json'}

        post_response = requests.request("POST", url, data=payload, headers=headers)

        print(post_response.text)
        # Convert the response from JSON to Python
        jsonResponse = json.loads(post_response.text)
        jr = jsonResponse[0] # Short hand jsonResponse[0] since it will be used a lot

        # Get all the meta-data for the game
        # All of these are wrapped in a try loop as many
        # items do not have meta-data such as developer or release date.
        # Frequently this occurrs on non-base game items like a DLC

        # Cover
        try:
            cover = jr["cover"]["image_id"]
        except Exception as e:
            cover = None

        # Base_Game
        base_game = False
        if jr["category"] in [0, 3, 8, 9, 10]: #IDS TO DETERMINE IF A GAME IS A BASE GAME OR NOT
            base_game = True

        # Release_Date
        try:
            mS = int(jr["release_dates"][0]["date"])
            release_date = datetime.utcfromtimestamp(mS).strftime('%Y-%m-%d')
        except Exception as e:
            release_date = None

        # Genres
        try:
            genres = ""
            for genre in jr["genres"]:
                genres += genre["name"] + "|"
            genres = genres[:-1]
        except Exception as e:
            genres = None

        # Themes
        try:
            themes = ""
            for theme in jr["themes"]:
                name = theme["name"]
                # Trim IGDB's 4X theme name
                if "4X" in name:
                    name = "4X"
                themes += name + "|"
            themes = themes[:-1]
        except Exception as e:
            themes = None

        # Game Modes
        try: 
            game_modes = ""
            for mode in jr["game_modes"]:
                game_modes += mode["name"] + "|"
            game_modes = game_modes[:-1]
        except Exception as e:
            game_modes = None

        # Developer
        try:
            developers = ""
            for company in jr["involved_companies"]:
                if company["developer"] == True:
                    devName = company["company"]["name"]
                    devName = devName.replace(",", "")
                    developers += devName + "|"
            developers = developers[:-1]
        except Exception as e:
            developers = None

        # Add the new game
        newGame = Game(
            id=id,
            title=title,
            cover=cover,
            base_game=base_game,
            release_date=release_date,
            genre=genres,
            theme=themes,
            play_mode=game_modes,
            developer=developers
        )
        db.session.add(newGame)
        db.session.commit()
        print(str(newGame.title) + " IS BEING ADDED")

    returnArr = {'id':request.form['id']}
    return returnArr