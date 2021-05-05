"use strict";

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

  $.get('/api/homepage', (locations) => {
    for (const location of locations) {
      // Define the content of the infoWindow
      const locationInfoContent = (`
      <div class="window-content">
        <div class="location-thumbnail">
          <img
            src=${location.image}
            alt='Image of ${location.name}'
          />
        </div>

        <ul class="location-info">
          <li><b>${location.name}</b></li>
          <li>${location.description}</li>
        </ul>
      </div>
    `);

    const locationMarker = new google.maps.Marker({
      position: {
        lat: location.latitude,
        lng: location.longitude
      },
      title: `Location: ${location.locationID}`,
      map: map,
    });

    locationMarker.addListener('click', () => {
      locationInfo.close();
      locationInfo.setContent(locationInfoContent);
      locationInfo.open(map, locationMarker);
    });
  }
});
};


