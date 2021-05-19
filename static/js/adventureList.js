// Add location to list

function addItem() {
    let a = document.getElementById("adventure-list");
    let addLocationName = document.getElementById("add-location-name");
    let li = document.createElement("li");
    li.setAttribute('id', addLocationName.value);
    li.appendChild(document.createTextNode(addLocationName.value));
    a.appendChild(li);
    $.post({
        url: '/api/add_to_list',
        data: {location_id: locationId},
        success: function(){
            console.log('Add to list returned success code.');
            window.location.href = "/adventure_list";
        },
        error: function(){
            console.log('Add to list returned failure code.');
            window.location.href = "/sign_me_up";
        }
    });  
}

// Remove item from list

function removeItem() {

    let a = document.getElementById("adventure-list");
    let addLocationName = document.getElementById("add-location-name");
    let item = document.getElementById(addLocationName.value);
    a.removeChild(item);
}