"""Script to seed database."""
import os
import json
import crud
import model
import server

os.system('dropdb --if-exists adventurespark')
os.system('createdb adventurespark')

model.connect_to_db(server.app)
model.db.create_all()

crud.create_user('test', 'test@test.com', 'test')

with open('data/locations.json') as f:
    location_data = json.loads(f.read())

locations_in_db = []
for location in location_data:
    location_name, lat, long, desc = (location['location_name'],
                                                location['lat'],
                                                location['long'],
                                                location['desc'])
    db_location = crud.create_location(location_name, lat, long, desc)
    locations_in_db.append(db_location)

crud.create_adventure(1, 2)
crud.create_adventure(1, 8)
crud.create_adventure(1, 30)
crud.create_adventure(1, 24)
crud.create_adventure(1, 5)
crud.create_adventure(1, 32)
crud.create_adventure(1, 33)
crud.create_adventure(1, 41)
