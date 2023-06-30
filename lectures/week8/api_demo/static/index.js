console.log("Running JS file");

function searchAPI(e) {
    e.preventDefault(); // Stop the page from refreshing
    var formElement = document.getElementById("searchForm");
    var attachedForm = new FormData(formElement);
    // Call on the FETCH API
    fetch("http://localhost:5000/search", { method : "POST", body: attachedForm})
    .then(response => response.json()) // Convert response to json data
    .then(rawData => { // Do something with the JSON data
        console.log(rawData);
        // Height of Pokemon
        var height = rawData.height; // OR rawData["height"]
        var name = rawData["species"]["name"]; // OR rawData.species.name
        var frontDefaultURL = rawData['sprites']['front_default'];
        var frontShinyDefaultURL = rawData['sprites']['front_shiny'];
        // Grab on to the searchResults div
        var searchResultsDiv = document.getElementById("searchResults");
        // Clear the div out for new search data
        searchResultsDiv.replaceChildren();
        // Create some HTML elements to put in the div
        // Create the name
        var nameTag = document.createElement("h2");
        nameTag.innerText = "Name: " + name;
        searchResultsDiv.appendChild(nameTag);
        // Height
        var heightTag = document.createElement("p");
        heightTag.innerText = "Height: " + height;
        searchResultsDiv.appendChild(heightTag);
        // Front default image
        var frontDefaultImgTag = document.createElement("img")
        frontDefaultImgTag.src = frontDefaultURL;
        searchResultsDiv.appendChild(frontDefaultImgTag);
        // Front default shiny image
        var frontShinyDefaultImgTag = document.createElement("img")
        frontShinyDefaultImgTag.src = frontShinyDefaultURL;
        searchResultsDiv.appendChild(frontShinyDefaultImgTag);

    })
}