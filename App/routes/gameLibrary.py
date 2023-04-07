from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from ..models.uGameModels import UserGame
from ..models.gameModels import Game
from ..models import db

bp = Blueprint('gameLibrary', __name__)

@bp.route('/updategamevalue', methods=['GET', 'POST'])
def update_game_value():
    # Pull game based on passed through ID. 
    game = UserGame.query.filter_by(user_id=current_user.id, game_id=request.form['id']).first()
    newVal = request.form['value']
    typeOfMod = request.form['typeOfMod']

    if typeOfMod == "time":
        game.hours_played = newVal
    elif typeOfMod == "progress":
        game.play_status = newVal
    elif typeOfMod == "rating":
        match newVal:
            case "one":
                game.rating = 1
            case "two":
                game.rating = 2
            case "three":
                game.rating = 3
            case "four":
                game.rating = 4
            case "five":
                game.rating = 5
            case _:
                print("Invalid game rating provided")

    db.session.commit()

    return {'id':game.id, 'typeOfMod':typeOfMod, 'val':newVal, 'success':True}

@bp.route('/gamelibrary', methods=['GET', 'POST'])
@login_required
def game_library():
    #checks for post request, if there is one it must be for removal
    if request.method == "POST":
        #The worst code ever written, but copypasted. see userWishlist.py
        output = request.form.to_dict()
        game_list = list(output)
        lib_id = game_list[0]
        request_type = output[str(lib_id)]
        print(str(lib_id))
        print(request_type)
        if request_type == "Remove from Library":
            removedGame = UserGame.query.filter_by(user_id=current_user.id, game_id=lib_id).first()
            if removedGame:
                removedGame.archived = True
                db.session.commit()

    library = UserGame.query.filter(
        UserGame.user_id == current_user.id,
        UserGame.archived.is_not(True), 
        UserGame.wishlist.is_not(True)
    ).all() # Get all the user's games via their id
    game_ids = [g.game_id for g in library] # Store all the ID's for the user's games in a list variable
    game_list = Game.query.filter(Game.id.in_(game_ids)).all() # Get all games with an ID in the list
    playtime_list = []
    gamecomp_list = []
    gamerating_list = []
    #apologies for the backwards method of grabbing game time played, had to utilize
    #the game_list to make sure the playtime list was properly aligned.
    for i in game_list:
        hours = UserGame.query.filter(UserGame.user_id == current_user.id, UserGame.game_id == i.id).first().hours_played
        if hours is None:
            hours = 0.0
        playtime_list.append(hours)
        gamecomp_list.append(UserGame.query.filter(UserGame.user_id == current_user.id,
                                                   UserGame.game_id == i.id).first().play_status)
        
        rating = UserGame.query.filter(UserGame.user_id == current_user.id, UserGame.game_id == i.id).first().rating
        if rating is None:
            rating = "Not Rated"
        else:
            rating = str(rating) + "/5"
        gamerating_list.append(rating)

    return render_template("game-library.html", library=library, game_list=game_list, playtime_list = playtime_list, 
                           gamecomp_list = gamecomp_list, gamerating_list = gamerating_list)