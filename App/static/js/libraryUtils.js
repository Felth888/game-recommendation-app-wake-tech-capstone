/**
 * Library Utils
 * 
 * Contains functions and the public var "LIBRARY_IDS_ARR" for use in generating and editing a user's library.
 * LIBRARY_IDS_ARR is populated on page load if supplied with a "library_id_list" to its template.
 * 
 * REQUIRES UTILS.JS TO FUNCTION.
 */

// ID's variable, defaults as empty
var LIBRARY_IDS_ARR = [];

/**
 * Create logged in user's game library from the string passed to the page
 * LIBRARY_IDS_ARR is always available to be called, but will remain empty until 
 * this function is utilized with a string. Due to a Flask limitation, this must be called 
 * with the parameter present if in an external file.
 * @param {string} game_ids_string String of game ID's. Formatted <id>|<id>|<id>...
 */
function setLibraryIDArray(game_ids_string) {
    // Split the user's game library ID's string into an array
    if(game_ids_string && game_ids_string !== "") {
        LIBRARY_IDS_ARR = game_ids_string.split("|")
    }
    // Convert all the string ID's to int's if there is games in the user's library
    for(i = 0; i < LIBRARY_IDS_ARR.length; i++) {
        LIBRARY_IDS_ARR[i] = parseInt(LIBRARY_IDS_ARR[i]);
    }
}


/**
 * Adds the specific game to the user's wishlist. 
 * @param {int} id - IGDB of the game wanting to be added
 * @param {string} name - IGDB name of the game wanting to be added
 */
async function addToWishlist(id, name) {
    // If game doesnt exist in library, add it
    sendAjaxQuery('/update_library', 'id=' + id, false);

    var response = sendAjaxQuery('/add_to_wishlist', 'id=' + id, false);
    console.log("WISHLISTED: " + response);
}


/**
 * Adds the specific game to the user's library. 
 * @param {int} id - IGDB of the game wanting to be added
 * @param {string} name - IGDB name of the game wanting to be added
 */
async function addToLibrary(id, name) {
    
    // If game doesnt exist in library, add it
    sendAjaxQuery('/update_library', 'id=' + id + "&title=" + name, false);

    // Current check to see if the call is to add to library or remove
    var adding = 'true';
    if(LIBRARY_IDS_ARR.includes(id)) { adding = 'false'; }

    // Build query string to send to ajax query
    var queryString = 'id=' + id + '&adding=' + adding;
    
    // Send ajax and get the result
    var response = sendAjaxQuery('/add_to_library', queryString, false);

    // Modify the contents of the button to show add/remove based on response
    // Also add/remove the ID to the Library list. This prevents a need for a page refresh
    if(response['added']) {
        ID('lib_' + response['id']).innerHTML = "Remove from Library";
        // Add the ID from the list of session list of ID's
        LIBRARY_IDS_ARR.push(id);
    } else {
        ID('lib_' + response['id']).innerHTML = "Add to Library";
        // Remove the ID from the list of session list of ID's
        LIBRARY_IDS_ARR.splice(LIBRARY_IDS_ARR.indexOf(id), 1);
    }
}