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
        #The worst code ever written, but copypasted. see userWishlist.py
        output = request.form.to_dict()
        game_list = list(output)
        lib_id = game_list[0]
        removedGame = UserGame.query.filter_by(game_id=lib_id).first()
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
        
    return render_template("game-library.html", library=library, game_list=game_list)