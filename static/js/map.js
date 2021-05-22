"use strict";

function addToList(button){
  let locationId = button.getAttribute('data-location-id');
  console.log(locationId);
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
};

//Google Map functions

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    mapId: "40d6a623f18f9a8e",
    center: { lat: 51.507351, lng: -0.127758 },
    zoom: 5,
    scrollwheel: true,
    zoomControl: true,
    panControl: false,
    streetViewControl: false,
    fullscreenControl: false,
    mapTypeControl: false
  });

  const locationInfo = new google.maps.InfoWindow();

  $.get('/api/locations', (locations) => {
    for (const location of locations) {
      // Define the content of the infoWindow
      const locationInfoContent = `
        <div class="window-content">
          <div class="location-thumbnail">
            <img
              src=${location.image}
              alt='Image of ${location.name}'
            />
          </div>

          <div class="location-information">
            <h4>${location.name}</h4>
            <p>${location.description}</p>
            <div class="d-flex justify-content-center">
              <button type="button" class="btn btn-primary btn-sm px-3" data-location-id="${location.id}" onclick="addToList(this)">Add To List</button>
            </div>
          </div>
        </div>
      `;

      const locationMarker = new google.maps.Marker({
        position: {
          lat: location.latitude,
          lng: location.longitude
        },
        title: `${location.name}`,
        map: map,
        icon: "/static/img/bulb-icon.png"
      });

      locationMarker.addListener('click', () => {
        locationInfo.close();
        locationInfo.setContent(locationInfoContent);
        locationInfo.open(map, locationMarker);
        getVideo(location.name, location.id);
      });

    }
  });
};


