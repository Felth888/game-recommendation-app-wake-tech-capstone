from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from ..models.uGameModels import UserGame
from ..models.gameModels import Game
from ..models import db


bp = Blueprint('userWishlist', __name__)

@bp.route('/wishlist', methods=['GET', 'POST'])
@login_required
def wishlist():
    #if request method is POST, must be either a request to move to Library, or to remove from Wishlist
    if request.method == "POST":
        #The worst code ever written.
        #request.form returns form's name and value respectively as a dictionary key and value pair, which need to be isolated
        output = request.form.to_dict()
        game_list = list(output)
        wish_id = game_list[0]
        request_type = output[str(wish_id)]
        if request_type == "Move to Library":
            movedGame = UserGame.query.filter_by(user_id=current_user.id, game_id=wish_id).first()
            if movedGame:
                movedGame.wishlist = None
                #have to clear archived status to fix a minor potential bug
                movedGame.archived = None
                db.session.commit()
        elif request_type == "Remove from Wishlist":
            removedGame = UserGame.query.filter_by(user_id=current_user.id, game_id=wish_id).first()
            if removedGame:
                removedGame.wishlist = None
                removedGame.archived = True
                db.session.commit()

    wishlist = UserGame.query.filter(UserGame.user_id == current_user.id, UserGame.wishlist == True).all()
    wishlist_id = [w.game_id for w in wishlist]
    w_list = Game.query.filter(Game.id.in_(wishlist_id)).all()
        
    return render_template("wishlist.html", w_list=w_list)