"""Script to seed database."""

import os
import json
from random import choice

import crud
import model
import server

os.system('dropdb locations')
os.system('createdb locations')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/locations.json') as f:
    location_data = json.loads(f.read())


locations_in_db = []
for location in location_data:
    location_name, lat, long, desc, search_key = (location['location_name'],
                                                location['lat'],
                                                location['long'],
                                                location['desc'],
                                                location['search_key'])

    db_location = crud.create_location(location_name, lat, long, desc, search_key)
    locations_in_db.append(db_location)