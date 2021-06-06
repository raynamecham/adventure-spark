"use strict";

// Add to list from map info window

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

// Google Map functions

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

  const input = document.getElementById("pac-input");
  const autocomplete = new google.maps.places.Autocomplete(input);
  autocomplete.bindTo("bounds", map);
  // Specify just the place data fields that you need.
  autocomplete.setFields(["place_id", "geometry", "name"]);
  map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
  const infowindow = new google.maps.InfoWindow();
  const infowindowContent = document.getElementById("infowindow-content");
  infowindow.setContent(infowindowContent);
  const marker = new google.maps.Marker({ map: map });
  marker.addListener("click", () => {
    infowindow.open(map, marker);
  });
  autocomplete.addListener("place_changed", () => {
    infowindow.close();
    const place = autocomplete.getPlace();

    if (!place.geometry || !place.geometry.location) {
      return;
    }

    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);
    }
    // Set the position of the marker using the place ID and location.
    marker.setPlace({
      placeId: place.place_id,
      location: place.geometry.location,
    });
    marker.setVisible(true);
    infowindowContent.children.namedItem("place-name").textContent = place.name;
    infowindowContent.children.namedItem("place-id").textContent =
      place.place_id;
    infowindowContent.children.namedItem("place-address").textContent =
      place.formatted_address;
    infowindow.open(map, marker);
  });

  const locationInfo = new google.maps.InfoWindow();

  $.get('/api/locations', (locations) => {
    for (const location of locations) {
      // InfoWindow content
      const locationInfoContent = `
        <div class="window-content">
          <div class="location-thumbnail">
            <img
              src=${location.image}
              alt='Image of ${location.name}'
            />
          </div>

          <div class="location-information">
            <h5>${location.name}</h5>
            <p>${location.description}</p>
            <div class="d-flex justify-content-center">
              <button type="button" class="btn btn-primary btn-sm mb-2" data-location-id="${location.id}" onclick="addToList(this)">Add To List</button>
            </div>
          </div>
        </div>
      `;

      // Map marker info
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


