from flask import Blueprint, render_template
from flask_login import login_required
from ..models.uGameModels import UserGame
from ..models.userModels import User


bp = Blueprint('gameLibrary', __name__)

@bp.route('/gamelibrary', methods=['GET', 'POST'])
@login_required
def game_library(user_id):
    library = UserGame.query.filter_by(user_id=user_id).first()
    render_template("game-library.html", library=library)