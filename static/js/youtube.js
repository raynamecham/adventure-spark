"use strict";

// Youtube functions

function getVideo(locationName, locationId) {
    $.get({
        url: '/api/youtube_cache',
        data: {location_id: locationId},
        success: function(getCacheData){
            console.log("YouTube_Cache GET Request Succeeded");
            if (getCacheData.items.length === 3) {
                console.log("YouTube_Cache Found Three Videos");
                embedVideo(getCacheData, locationName);
            }
            else {
                console.log("YouTube_Cache Did NOT Find Three Videos");
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
                    success: function(youTubeData){
                        console.log("YouTube Search Request Succeeded");
                        $.post({
                            url: '/api/youtube_cache',
                            data: {
                                items: JSON.stringify(youTubeData['items']),
                                location_id: locationId
                            },
                            success: function(){
                                console.log("YouTube_Cache POST Request Succeeded");
                                embedVideo(youTubeData, locationName)
                            },
                            error: function(response){
                                console.log("YouTube_Cache POST Request Failed");
                                console.log(response);
                            }
                        });
                    },
                    error: function(response){
                        console.log("YouTube Search Request Failed");
                        console.log(response);
                    }
                });
            }
        },
        error: function(response){
            console.log("YouTube_Cache GET Request Failed");
            console.log(response);
        }
    });
}

// Embed videos on page

function embedVideo(data, locationName) {
    // update videos-heading
    $('#videos-heading span.location-name').text(locationName);
    console.log('H4 Location Text Updated');

    for (let i = 0; i < data.items.length; i++) {
        $('#video' + i +' iframe').attr('src', 'https://www.youtube.com/embed/' + data.items[i].id.videoId);
        $('#video' + i +' p').text(data.items[i].snippet.title);
        console.log('Video '+(i+1)+' updated');
    }
}