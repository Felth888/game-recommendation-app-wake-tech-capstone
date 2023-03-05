from ..models.userModels import User
from ..models.uGameModels import UserGame
from ..models.gameModels import Game

# Creates the formatted library string for the user based on ID and returns it.
# Return is formatted as <id>|<id>... Empty string means no games in library
def getLibraryString(id):
    lib_games = []
    try:
        lib_games = UserGame.query.filter_by(user_id=id).all()
    except Exception as e:
        return "Error with query"

    # Only run the games list code if the user actually has games in their library.
    if len(lib_games) > 0:

        # Creates a string to pass to the search page formatted as id|id|id...
        lib_id_string = ""
        for game in lib_games:
            lib_id_string += str(game.game_id) + "|"
            #print("User " + str(current_user.user_name) + " has " + str(game.game_id) + " in their library.") #Uncomment for debug output
        # Removes the last not needed | from the string
        lib_id_string = lib_id_string[:-1]
        return lib_id_string
    
    return ""