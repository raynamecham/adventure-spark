// Add location to list

function addItem() {
    let a = document.getElementById("adventure-list");
    let addLocationName = document.getElementById("add-location-name");
    let li = document.createElement("li");
    li.setAttribute('id', addLocationName.value);
    li.appendChild(document.createTextNode(addLocationName.value));
    a.appendChild(li); 
}

// Remove item from list

function removeItem() {

    let a = document.getElementById("adventure-list");
    let addLocationName = document.getElementById("add-location-name");
    let item = document.getElementById(addLocationName.value);
    a.removeChild(item);
}