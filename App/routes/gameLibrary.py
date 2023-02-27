from flask import Blueprint, render_template
from flask_login import login_required
from ..models.uGameModels import UserGame
from ..models.userModels import User


bp = Blueprint('gameLibrary', __name__)

@bp.route('/gamelibrary', methods=['GET', 'POST'])
@login_required
def game_library(user_id):
    library = UserGame.query.filter_by(user_id=user_id).first()
    """
    1. list of dictionary objects
        each dictionary is an individual game
    pass that data to template
    within template, have a for each jinja loop:
    for each game in game_list:
        {{ game.title }}
        {{ game.cover }}
    """
    render_template("game-library.html", library=library)