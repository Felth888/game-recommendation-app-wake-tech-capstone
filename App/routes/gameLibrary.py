from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from ..models.uGameModels import UserGame
from ..models.gameModels import Game
from ..models import db

bp = Blueprint('gameLibrary', __name__)

@bp.route('/gamelibrary', methods=['GET', 'POST'])
@login_required
def game_library():
    #checks for post request, if there is one it must be for removal
    if request.method == "POST":
        print("Test")
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
        else:
            #This code will probably have to change if we impliment something in addition to playtime tracking.
            #Right now it relies on the fact that a post request that isn't for removing a game on the library page
            #must be for changing playtime.
            modifygame = UserGame.query.filter_by(user_id=current_user.id, game_id=lib_id).first()
            if modifygame:
                modifygame.hours_played = request_type
                db.session.commit()


    library = UserGame.query.filter(
        UserGame.user_id == current_user.id,
        UserGame.archived.is_not(True), 
        UserGame.wishlist.is_not(True)
    ).all() # Get all the user's games via their id
    game_ids = [g.game_id for g in library] # Store all the ID's for the user's games in a list variable
    game_list = Game.query.filter(Game.id.in_(game_ids)).all() # Get all games with an ID in the list
    playtime_list = []
    #appologies for the backwards method of grabbing game time played, had to utilize
    #the game_list to make sure the playtime list was properly aligned.
    for i in game_list:
        playtime_list.append(UserGame.query.filter(UserGame.user_id == current_user.id,
                                                   UserGame.game_id == i.id).first().hours_played)

    return render_template("game-library.html", library=library, game_list=game_list, playtime_list = playtime_list)