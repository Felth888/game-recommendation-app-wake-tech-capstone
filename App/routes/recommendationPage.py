from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from ..services.libraryUtils import getLibraryString, getWishlistString

bp = Blueprint('recommendationPage', __name__)

from ..models.userModels import User
from ..models.uGameModels import UserGame
from ..models.gameModels import Game

@bp.route('/recommendationpage', methods=['GET', 'POST'])
@login_required
def recommendationPage():
    lib_id_string = getLibraryString(current_user.id)
    wish_id_string = getWishlistString(current_user.id)
    return render_template('recommendation.html', title='Recommendations', library_id_list=lib_id_string, wishlist_id_list = wish_id_string)
    
@bp.route('/recommendCall', methods=['POST'])
def recommend():
    getGame = Game.query.filter_by(id=request.form['id']).first()
    returnArr = {
        'id':getGame.id, 
        'title':getGame.title,
        'cover':getGame.cover,
        'base_game':getGame.base_game,
        'release_date':getGame.release_date,
        'genre':getGame.genre,
        'theme':getGame.theme,
        'play_mode':getGame.play_mode,
        'developer':getGame.developer
    }
    return returnArr