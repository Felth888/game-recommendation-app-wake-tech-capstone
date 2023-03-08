from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models.uGameModels import UserGame
from ..models.gameModels import Game


bp = Blueprint('userWishlist', __name__)

@bp.route('/wishlist', methods=['GET', 'POST'])
@login_required
def wishlist():
    wishlist = UserGame.query.filter(UserGame.user_id == current_user.id, UserGame.wishlist == True).all()
    wishlist_id = [w.game_id for w in wishlist]
    w_list = Game.query.filter(Game.id.in_(wishlist_id)).all()
        
    return render_template("wishlist.html", w_list=w_list)