from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint('recommendationPage', __name__)

from ..models.userModels import User

@bp.route('/recommendationpage', methods=['GET', 'POST'])
def recommendationPage():
    if current_user.is_authenticated:
        return render_template('recommendation.html')
    
