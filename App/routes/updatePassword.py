from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

bp = Blueprint('updatePassword', __name__)
from ..models.userModels import User
from ..models import db
from ..services.forms import UpdatePasswordForm

@bp.route('/updatePasswordPage', methods=['GET', 'POST'])
@login_required
def updatePasswordPage():
    form = UpdatePasswordForm()
    print('\n')
    print(current_user.user_name)
    print(current_user.password)
    print('\n')
    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('loginPage.login'))
    # elif request.method == 'GET':
    #     pass
    return render_template('update-password.html', form=form, title='Update Password')