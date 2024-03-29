from . import db
from flask import current_app
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from time import time

from App import login



class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(32), unique=True)
    email = db.Column(db.String, unique=True)
    birthdate = db.Column(db.DateTime)
    password = db.Column(db.String(128))
    



    def is_active(self):
        return True

    def get_id(self):
        return self.email
    
    def set_password(self, password_to_hash):
        self.password = generate_password_hash(password_to_hash)

    def check_password(self, password_to_hash):
        return check_password_hash(self.password, password_to_hash)
    
    def get_reset_token(self, expires=500):
        return jwt.encode({'reset_password': self.user_name, 'exp': time() + expires}, current_app.config['JWT_SECRET'])



@login.user_loader 
def load_user(id):
    return User.query.filter_by(email=id).first()
