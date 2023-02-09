from flask import Blueprint, render_template
bp = Blueprint('newAccount', __name__)
from ..services.forms import NewAccountForm

@bp.route('/newaccount', methods=['GET', 'POST'])
def newAccountPage():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = NewAccountForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template("new-account.html", form=form)