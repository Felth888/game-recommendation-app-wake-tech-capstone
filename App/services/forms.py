
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from ..models.userModels import User



class LoginForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class NewAccountForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    birthday  = DateField('Your Birthday', format='%Y-%m-%d')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Retype Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class UpdateProfileForm(FlaskForm):
    user_name = StringField('Username', validators=[DataRequired()])
    birthday  = DateField('Your Birthday', format='%Y-%m-%d')
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Update')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')