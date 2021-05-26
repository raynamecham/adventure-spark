// Remove adventure from list

function deleteAdventure(button) {
    let adventureId = button.getAttribute('data-adventure-id');
    console.log(adventureId);
    $.post({
        url: '/api/delete_adventure',
        data: {adventure_id: adventureId},
        success: function(){
            console.log('deleteAdventure returned success code.');
            window.location.href = "/adventure_list";
        },
        error: function(){
            console.log('deleteAdventure returned failure code.');
        }
    });
}

// Moves checked item to "Adventures I've Had" list

function visitedAdventure() {
    let checkBox = document.getElementById("visit-adventure");

    if (checkBox.checked == true) {
        $.get({
            url: '/api/visit_adventure',
            data: {visited: checkBox},
            success: function(){
                console.log('visitedAdventure returned success code.');
            },
            error: function(){
                console.log('visitedAdventure returned failure code.');
            }
        });
    } else {
        console.log ('checkbox is unchecked');
    };
}