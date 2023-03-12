from ..models.userModels import User
from ..models.uGameModels import UserGame
from ..models.gameModels import Game
from flask_login import current_user

# Creates the formatted string of library games for the user based on ID and returns it.
# Return is formatted as <id>|<id>... Empty string means no games in library
def getLibraryString(id):
    lib_games = []
    try:
        # Filter conditions -> Matching user id, not archived, and not wishlisted
        lib_games = UserGame.query.filter(UserGame.user_id == id, UserGame.archived.is_not(True), UserGame.wishlist.is_not(True)).all()
    except Exception as e:
        return "Error with query"

    # Only run the games list code if the user actually has games in their library.
    if len(lib_games) > 0:
        return formatString(lib_games)

    return ""

# Creates the formatted string of wishlist games for the user based on ID and returns it but
# Return is formatted as <id>|<id>... Empty string means no games in wisnlist
def getWishlistString(id):
    wish_games = []
    try:
        # Filter conditions -> Matching user id, not archived, and not wishlisted
        wish_games = UserGame.query.filter(UserGame.user_id == id, UserGame.wishlist == True).all()
    except Exception as e:
        return "Error with query"

    # Only run the games list code if the user actually has games in their library.
    if len(wish_games) > 0:
        return formatString(wish_games)

    return ""

# Formats the string for a list of games by their ID's to form a string of <id>|<id>|<id>... 
def formatString(list):
    format_string = ""
    for game in list:
        format_string += str(game.game_id) + "|"
        #print(str(game.game_id) + " added") #Uncomment for debug output
    # Removes the last not needed | from the string
    format_string = format_string[:-1]
    return format_string