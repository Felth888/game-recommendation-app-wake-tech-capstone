from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from App import login



class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    email = db.Column(db.String, primary_key=True)
    birthdate = db.Column(db.DateTime)
    password_hash = db.Column(db.String(128))
    



    def is_active(self):
        return True

    def get_id(self):
        return self.email
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



@login.user_loader
def load_user(id):
    return User.query.get(int(id))
