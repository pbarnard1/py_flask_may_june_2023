console.log("Running JS file");

function searchAPI(e) {
    e.preventDefault(); // Stop the page from refreshing
    var formElement = document.getElementById("searchForm");
    var attachedForm = new FormData(formElement)
    // Call on the FETCH API
    fetch("http://localhost:5000/search", { method : "POST", body: attachedForm})
    .then(response => response.json()) // Convert response to json data
    .then(rawData => { // Do something with the JSON data
        console.log(rawData);
    })
}