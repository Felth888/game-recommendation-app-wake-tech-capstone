from . import db

class UserGame(db.Model):
    #accessing the user_games table
    #in game_database.sql
    __tablename__ = 'user_games'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True)
    game_id = db.Column(db.Integer, unique=True)
    play_status = db.Column(db.String(10))
    hours_played = db.Column(db.Float)
    rating = db.Column(db.Integer)
    wishlist = db.Column(db.Boolean)
    archived = db.Column(db.Boolean)
