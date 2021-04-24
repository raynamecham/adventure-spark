"use strict";

function initMap() {
    const seattleCoords = {
        lat: 47.6062,
        lng: 122.3321
    };

    const basicMap = new google.maps.Map (
        document.querySelector('#map'),
        {
            center: seattleCoords,
            zoom: 11
        }
    );
};