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
var WISHLIST_IDS_ARR = [];

/**
 * Create logged in user's game library from the string passed to the page
 * LIBRARY_IDS_ARR is always available to be called, but will remain empty until 
 * this function is utilized with a string. Due to a Flask limitation, this must be called 
 * with the parameter present if in an external file.
 * @param {string} library_id_string String of game ID's for the library. Formatted <id>,<id>,<id>...
 * @param {string} wishlist_id_string String of game ID's for the wishlist. Formatted <id>,<id>,<id>...
 */
function setIDArrays(library_id_string, wishlist_id_string) {
    // Split the user's game library ID's string into an array
    if(library_id_string && library_id_string !== "") {
        LIBRARY_IDS_ARR = library_id_string.split(",")
    }

    // Split the user's game wishlist ID's string into an array
    if(wishlist_id_string && wishlist_id_string !== "") {
        WISHLIST_IDS_ARR = wishlist_id_string.split(",")
    }

    // Convert all the string ID's to int's if there is games in the user's library
    for(i = 0; i < LIBRARY_IDS_ARR.length; i++) {
        LIBRARY_IDS_ARR[i] = parseInt(LIBRARY_IDS_ARR[i]);
    }

    // Convert all the string ID's to int's if there is games in the user's wishlist
    for(i = 0; i < WISHLIST_IDS_ARR.length; i++) {
        WISHLIST_IDS_ARR[i] = parseInt(WISHLIST_IDS_ARR[i]);
    }
}


/**
 * Adds the specific game to the user's wishlist. 
 * @param {int} id - IGDB of the game wanting to be added
 * @param {string} name - IGDB name of the game wanting to be added
 * @return {bool} Returns whether something was added or not. True for added, false for removed. 
 */
function addToWishlist(id, name) {
    
    // If the game is in the user's library, it cannot be added to their wishlist
    if(LIBRARY_IDS_ARR.includes(id)) {
        return null;
    }

    // If game doesnt exist in the database, add it
    sendAjaxQuery('/update_catalog', 'id=' + id + "&title=" + name, false);

    // Current check to see if the call is to add to wishlist or remove
    var adding = 'true';
    if(WISHLIST_IDS_ARR.includes(id)) { adding = 'false'; }

    // Build query string to send to ajax query
    var queryString = 'id=' + id + '&adding=' + adding;
    
    // Send ajax and get the result
    var response = sendAjaxQuery('/add_to_wishlist', queryString, false);

    // Add/remove the ID to the Wishlist list. This prevents a need for a page refresh
    if(response['added']) {
        // Add the ID from the list of session list of ID's
        WISHLIST_IDS_ARR.push(id);
    } else {
        // Remove the ID from the list of session list of ID's
        WISHLIST_IDS_ARR.splice(WISHLIST_IDS_ARR.indexOf(id), 1);
    }

    // Return the response true/false for adding to update the button in the html file
    return response['added'];
}


/**
 * Adds the specific game to the user's library. 
 * @param {int} id - IGDB of the game wanting to be added
 * @param {string} name - IGDB name of the game wanting to be added
 * @return {bool} Returns whether something was added or not. True for added, false for removed. 
 */
function addToLibrary(id, name) {
    
    // Replace '&' in game title as it is used in URL's to denotate arguments. %26 is the HTML encoded equivelant
    name = name.replace("&", "%26");
    
    // If game doesnt exist in database, add it
    sendAjaxQuery('/update_catalog', 'id=' + id + "&title=" + name, false);

    // Current check to see if the call is to add to library or remove
    var adding = 'true';
    if(LIBRARY_IDS_ARR.includes(id)) { adding = 'false'; }

    // Build query string to send to ajax query
    var queryString = 'id=' + id + '&adding=' + adding;
    
    // Send ajax and get the result
    var response = sendAjaxQuery('/add_to_library', queryString, false);

    // Add/remove the ID to the Library list. This prevents a need for a page refresh
    if(response['added']) {
        // Add the ID from the list of session list of ID's
        LIBRARY_IDS_ARR.push(id);
        // Remove the ID from the user's wishlist list if present
        if(WISHLIST_IDS_ARR.includes(id)) {
            WISHLIST_IDS_ARR.splice(WISHLIST_IDS_ARR.indexOf(id), 1);
        }
    } else {
        // Remove the ID from the list of session list of ID's
        LIBRARY_IDS_ARR.splice(LIBRARY_IDS_ARR.indexOf(id), 1);
    }

    // Return the response true/false for adding to update the button in the html file
    return response['added'];
}