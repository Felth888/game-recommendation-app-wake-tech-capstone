from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models.uGameModels import UserGame
from ..models.gameModels import Game


bp = Blueprint('gameLibrary', __name__)

@bp.route('/gamelibrary', methods=['GET', 'POST'])
@login_required
def game_library():
    library = UserGame.query.filter_by(user_id=current_user.id).first()
    game_id = Game.query.filter_by(id=UserGame.game_id)
    game_list = []

    for game in game_id:
        game_list.append(game)
        
    render_template("game-library.html", library=library, game_list=game_list)