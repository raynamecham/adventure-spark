// Youtube functions

function getVideo(locationName) {
    $.get({
        url: 'https://www.googleapis.com/youtube/v3/search',
        data: {
            key: 'AIzaSyBOk3yXP1PNSBExCoO6Vh0-o7mTUElZWAY',
            q: 'things to do ' + locationName,
            part: 'snippet',
            maxResults: 3,
            type: 'video',
            videoEmbeddable: true
        },
        success: function(data){
            embedVideo(data, locationName)
        },
        error: function(response){
            console.log("Request Failed");
            console.log(response);
        }
    });
}

function embedVideo(data, locationName) {
    // update videos-heading
    $('#videos-heading span.location-name').text(locationName);

    for (let i = 0; i < data.items.length; i++) {
        $('#video' + i +' iframe').attr('src', 'https://www.youtube.com/embed/' + data.items[i].id.videoId);
        $('#video' + i +' p').text(data.items[i].snippet.title);
    }
}