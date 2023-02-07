from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PhoneNumber

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    user_name = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birthdate = db.Column(db.DateTime)
    zipcode = db.Column(db.Integer)

    phone_number = db.Column(db.Unicode(255))
    phone_country_code = db.Column(db.Unicode(8))

    phone_number = db.composite(
        PhoneNumber,
        phone_number,
        phone_country_code
    )

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False