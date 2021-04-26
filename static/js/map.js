"use strict";

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    center: {
      lat: 47,
      lng: 122
    },
    scrollwheel: true,
    zoom: 2,
    zoomControl: true,
    panControl: true,
    streetViewControl: false
  });

  const locationInfo = new google.maps.InfoWindow();

  $.get('/api/locations', (locations) => {
    for (const location of locations) {
      // Define the content of the infoWindow
      const locationInfoContent = (`
      <div class="window-content">
        <div class="location-thumbnail">
          <img
            src="/static/img/placeholder.png"
            alt="placeholder"
          />
        </div>

        <ul class="location-info">
          <li>${location.locationName}</li>
        </ul>
      </div>
    `);

    const locationMarker = new google.maps.Marker({
      position: {
        lat: location.lat,
        lng: location.long
      },
      title: `Location: ${location.locationID}`,
      icon: {
        url: '/static/img/placeholder.png',
        scaledSize: new google.maps.Size(50, 50)
      },
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