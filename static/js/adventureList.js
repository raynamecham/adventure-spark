"use strict";

// Remove adventure from list

function deleteAdventure(button) {
    let adventureId = button.getAttribute('data-adventure-id');
    console.log(adventureId);
    $.post({
        url: '/api/delete_adventure',
        data: {adventure_id: adventureId},
        success: function(){
            console.log('deleteAdventure returned success code.');
            location.reload();
        },
        error: function(){
            console.log('deleteAdventure returned failure code.');
        }
    });
}

// Move adventures between visited and not visited

function updateAdventure(checkbox) {
    let adventureId = checkbox.getAttribute('data-adventure-id');
    let visited = checkbox.getAttribute('data-visited');
    let oppositeVisited;

    if (visited == "False") {
        oppositeVisited = "True";
    }
    else {
        oppositeVisited = "False";
    }

    $.post({
        url: '/api/update_adventure',
        data: {
            "adventure_id": adventureId,
            "visited": oppositeVisited
        },
        success: function(){
            console.log('updateAdventure returned success code.');
            location.reload();
        },
        error: function(){
            console.log('updateAdventure returned failure code.');
        }
    });
}