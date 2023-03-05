from . import db

class Game(db.Model):
    #accessing the games table
    #in game_database.sql
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    cover = db.Column(db.Text)
    dlc = db.Column(db.Boolean)
    age_rating = db.Column(db.String(5))
    release_date = db.Column(db.DateTime)