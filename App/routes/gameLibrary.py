from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models.uGameModels import UserGame
from ..models.gameModels import Game


bp = Blueprint('gameLibrary', __name__)

@bp.route('/gamelibrary', methods=['GET', 'POST'])
@login_required
def game_library():
    library = UserGame.query.filter_by(user_id=current_user.id).all() # Get all the user's games via their id
    game_ids = [g.game_id for g in library] # Store all the ID's for the user's games in a list variable
    game_list = Game.query.filter_by(Game.id.in_(game_ids)).all() # Get all games with an ID in the list 
        
    return render_template("game-library.html", library=library, game_list=game_list)