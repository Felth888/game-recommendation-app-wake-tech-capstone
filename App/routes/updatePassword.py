from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_login import current_user
from flask_mail import Mail, Message
import jwt

bp = Blueprint('updatePassword', __name__)
from ..models.userModels import User
from ..models import db
from ..services.forms import UpdatePasswordForm, RequestEmailForm


@bp.route('/updatePasswordPage', methods=['GET', 'POST'])
@bp.route('/updatePasswordPage/<token>', methods=['GET', 'POST'])
def updatePasswordPage(token=None):

    tokenUser = verify_reset_token(token)

    if tokenUser is None:
        print("NO USER FOUND")
    else:
        print(tokenUser)

    # Create the password reset form
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        # If the user is logged in, just changed the logged in user's password
        if current_user.is_authenticated:
            current_user.set_password(form.password.data)
        # If they are not logged in, use the token from the email  
        else:
            user = User.query.filter_by(email=tokenUser.email).first()
            user.set_password(form.password.data)

        # commit changes
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('loginPage.login'))
    
    # Setup email request form for non-logged in users
    emailForm = RequestEmailForm()
    if emailForm.validate_on_submit():
        # Get the user based on their email
        user = User.query.filter_by(email=emailForm.email.data).first()
        # Check to see if the user exists. If so, send the email
        if user is not None:

            userToken = user.get_reset_token()
            print("\n\nUSER TOKEN: " + userToken + "\n\n")
            mail = Mail(current_app)
            mail.init_app(current_app)

            msg = Message()
            msg.subject = "PlayThis: Password Reset Request"
            msg.recipients = [user.email]
            msg.sender = current_app.config['MAIL_USERNAME']
            msg.body=f'''
            To reset your password, please click the following link. If you did not request a password reset, ignore this email.

            {url_for('updatePassword.updatePasswordPage', token=userToken, _external=True)}
            '''

            mail.send(msg)
        # Return the "We'll send an email if the account exists" page. Don't confirm/deny the email existed for security 
        return render_template('request-email.html', form=emailForm, submitted=True, title='Update Password')

    if current_user.is_authenticated or tokenUser is not None:
        return render_template('update-password.html', form=form, title='Update Password')
    else:
        return render_template('request-email.html', form=emailForm, title='Update Password')
    

def verify_reset_token(token):
    try:
        username = jwt.decode(token, key=current_app.config['JWT_SECRET'], verify=False, options={'verify_signature': False})['reset_password']
    except Exception as e:
        print("\n\nERROR:")
        print(e)
        print("\n\n")
        return None
    return User.query.filter_by(user_name=username).first()