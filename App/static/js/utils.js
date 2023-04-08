/**
 * Utils
 * 
 * Contains functions for general use such as a shorthand AJAX call via JQuery.
 * 
 * REQUIRES JQUERY 3.6.3 TO FUNCTION.
 */

/**
 * Uses AJAX to send a POST request to the flask backend at a specific URL with a given data.
 * Allows for a POST request without refreshing the page.
 * @param {string} urlIn - The URL to send the POST request to
 * @param {string} dataIn - The data string in to be sent in the post request. Formatted in standard URL-encoded notation
 * @param {bool} conOut - Post query response to console. Used for debugging purposes, recommended to be left off.
 * @return {string} Returns the response, allowing it to be checked or compared
 */
function sendAjaxQuery(urlIn, dataIn, conOut) {
    var r;
    $.ajax({
        url: urlIn, // Param 1
        data: dataIn, // Param 2
        dataType: 'json', // Data is returned as a json array. Parse as needed
        type: 'POST',
        async: false, // Forced async to be disabled to allow for returning the response
        success: function(response){
            r = response;
        },
        error: function(error){
            r = response;
        }
    });
    if(conOut) { console.log(r); }
    return r;
}


/**
 * Function to short-hand the getElementById function
 * @returns HTML element
 */
var ID = function(elementID) {
    return document.getElementById(elementID);
}



/**
 * Creates a promise and sets it on a timeout of the given millisecond value. 
 * Used with an 'await' to pause asynchronous functions if needed.
 * Ex: Pausing a function to allow a DOM's display change to appear
 * @param {int} milliseconds The number of milliseconds to delay
 * @return {Promise} A promise response set to trigger after provided milliseconds 
 */
function delay(milliseconds){
    return new Promise(resolve => {
        setTimeout(resolve, milliseconds);
    });
}

/**
 * Creates a table of arr's data points, using valString to 
 * specify an index for data to fill the cell with. Used to create
 * a table from a JSON array containing objects with fields.
 *
 * @param {array} arr - The array to be passed in
 * @param {string} valString - The index of the array item to pull data from
 * @return {string} String containing an entire table with cells formed from 'arr' content's specified index 
 */
function createTableFromVal(arr, valString) {

    var tableString = "<div>";
    // Doesnt pull data from empty endpoints (such as no platform)
    if(typeof arr != "undefined") {
        // Loop through each value and add a table cell
        var counter = arr.length;
        for (j = 0; j < counter; j++) {
            tableString += "<p>";
            tableString += "" + arr[j][valString] + "</p>";
        }
        tableString += "</div>";
    } else {
        // Add a filler 'Not Available' so there is no empty cells
        tableString += "<p>Not Available</p></div>";
    }
    
    return tableString;

}

/**
 * Custom handling for UI output
 * @param {string} input The message to convey to the user
 */
function alertUser(input) {
    alert(input);
}


