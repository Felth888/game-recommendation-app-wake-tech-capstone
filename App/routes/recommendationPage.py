from flask import Blueprint, render_template, request
from flask_login import current_user, login_required

from ..services.libraryUtils import getLibraryString

bp = Blueprint('recommendationPage', __name__)

from ..models.userModels import User
from ..models.uGameModels import UserGame
from ..models.gameModels import Game

@bp.route('/recommendationpage', methods=['GET', 'POST'])
@login_required
def recommendationPage():
    lib_id_string = getLibraryString(current_user.id)
    print("Games: " + lib_id_string)
    return render_template('recommendation.html', title='Recommendations', library_id_list=lib_id_string)
    
@bp.route('/recommendCall', methods=['POST'])
def recommend():
    getGame = Game.query.filter_by(id=request.form['id']).first()
    returnArr = {
        'id':getGame.id, 
        'title':getGame.title, 
        'cover':getGame.cover,
        'dlc':getGame.dlc,
        'age_rating':getGame.age_rating,
        'release_date':getGame.release_date
    }
    return returnArr