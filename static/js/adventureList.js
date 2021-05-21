// Add location to list

function addItem() {
    let a = document.getElementById("adventure-list");
    let addLocationName = document.getElementById("add-location-name");
    let li = document.createElement("li");
    $.post({
    url: '/api/add_user_location',
    data: {location_id: locationId, user_id: userId},
    success: function(){
        console.log('Add to list returned success code.');
        window.location.href = "/adventure_list";
        },
    error: function(){
        console.log('Add to list returned failure code.');
        }
    });
    li.setAttribute('id', addLocationName.value);
    li.appendChild(document.createTextNode(addLocationName.value));
    a.appendChild(li); 
}

// Remove item from list

function removeItem() {

    let a = document.getElementById("adventure-list");
    let addLocationName = document.getElementById("add-location-name");
    let item = document.getElementById(addLocationName.value);
    $.get({
    url: '/api/delete_adventure'

    });
    a.removeChild(item);
}