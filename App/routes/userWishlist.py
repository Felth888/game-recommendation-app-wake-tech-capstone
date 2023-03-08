from flask import Blueprint, render_template
from flask_login import login_required, current_user
from ..models.uGameModels import UserGame
from ..models.gameModels import Game


bp = Blueprint('userWishlist', __name__)

@bp.route('/wishlist', methods=['GET', 'POST'])
@login_required
def wishlist():
    library = UserGame.query.filter_by(user_id=current_user.id).all() # Get all the user's games via their id
    wishlist_id = []
    for w in library:
        if w.wishlist:
            wishlist_id.append(w.game_id)
    w_list = Game.query.filter(Game.id.in_(wishlist_id)).all()
    #game_ids = [g.game_id for g in library] # Store all the ID's for the user's games in a list variable
    #game_list = Game.query.filter(Game.id.in_(game_ids)).all() # Get all games with an ID in the list 
        
    return render_template("wishlist.html", library=library, w_list=w_list)