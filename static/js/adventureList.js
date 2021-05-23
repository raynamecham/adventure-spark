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