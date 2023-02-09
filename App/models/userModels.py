
from flask_login import UserMixin


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    user_name = db.Column(db.String(32))
    email = db.Column(db.String)
    birthdate = db.Column(db.DateTime)
    password_hash = db.Column(db.String(128))
    



    def is_active(self):
        return True

    def get_id(self):
        return self.email

