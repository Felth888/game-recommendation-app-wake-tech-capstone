from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
bp = Blueprint('userProfile', __name__)
from ..models.userModels import User
from ..services.forms import UpdateProfileForm
from ..models import db


@bp.route('/profile/<user_name>', methods=['GET', 'POST'])
@login_required
def profile(user_name):
    user = User.query.filter_by(user_name=user_name).first_or_404()
    return render_template("user-profile.html", user=user)


@bp.route('/update_profile', methods=['GET', 'POST'])
@login_required
def update_profile():
    form = UpdateProfileForm()
    if form.validate_on_submit():
        current_user.user_name = form.user_name.data
        current_user.birthdate = form.birthday.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('userProfile.profile', user_name=current_user.user_name))
    elif request.method == 'GET':
        form.user_name.data = current_user.user_name
        form.birthday.data = current_user.birthdate
    return render_template('update-profile.html', title='Update Profile',
                           form=form)