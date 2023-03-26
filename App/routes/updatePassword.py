from flask import Blueprint, render_template, request, flash, redirect, url_for

bp = Blueprint('updatePassword', __name__)
from ..models.userModels import User, load_user
from ..models import db
from ..services.forms import UpdatePasswordForm

@bp.route('/updatePasswordPage', methods=['GET', 'POST'])
def updatePasswordPage():
    form = UpdatePasswordForm()
    if form.validate_on_submit:
        print("\n\n\n\nVALIDATED FORM\n\n\n\n")
        user = load_user("user2@gmail.com")
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('loginPage.login'))
    return render_template('update-password.html', form=form, title='Update Password')