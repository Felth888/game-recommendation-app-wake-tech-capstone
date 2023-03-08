from . import db

class Game(db.Model):
    #accessing the games table
    #in game_database.sql
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    cover = db.Column(db.Text)
    base_game = db.Column(db.Boolean)
    release_date = db.Column(db.DateTime)
    genre = db.Column(db.Text)
    theme = db.Column(db.Text)
    play_mode = db.Column(db.Text)
    developer = db.Column(db.Text)
