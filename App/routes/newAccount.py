from flask import Blueprint, render_template, flash, redirect, url_for, request
bp = Blueprint('newAccount', __name__)
from ..services.forms import NewAccountForm
from flask_login import current_user

from ..models import db
from ..models.userModels import User


@bp.route('/newaccount', methods=['GET', 'POST'])
def newAccountPage():
    if current_user.is_authenticated:
        return redirect(url_for('searchPage.searchPage'))
    form = NewAccountForm()
    if form.validate_on_submit():
        user = User(user_name=form.user_name.data, email=form.email.data, birthdate=form.birthday.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you have made an account!')
        return redirect(url_for('loginPage.login'))
    return render_template("new-account.html", form=form, title="New Account")