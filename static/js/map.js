"use strict";

//Google Map functions

function initMap() {
  const map = new google.maps.Map(document.getElementById("map"), {
    mapId: "7c96088359f57898",
    center: { lat: 51.507351, lng: -0.127758 },
    zoom: 5,
    scrollwheel: true,
    zoomControl: true,
    panControl: false,
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
        lat: location.latitude,
        lng: location.longitude
      },
      title: `Location: ${location.locationID}`,
      icon: {
        scaledSize: new google.maps.Size(20, 20)
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


