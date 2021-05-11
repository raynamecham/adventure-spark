"""Script to seed database."""
import os
import json
import crud
import model
import server

os.system('dropdb adventurespark')
os.system('createdb adventurespark')

model.connect_to_db(server.app)
model.db.create_all()

crud.create_user('admin', 'admin@admin.com', 'admin')

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

crud.create_adventure(1, 3)
crud.create_adventure(1, 1)
crud.create_adventure(1, 4)
crud.create_adventure(1, 2)

crud.create_youtube_record('gdZLi9oWNZg', 'Video Title 1', 3)
crud.create_youtube_record('7C2z4GqqS5E', 'Video Title 2', 3)
crud.create_youtube_record('xEeFrLSkMm8', 'Video Title 3', 3)
crud.create_youtube_record('KhTeiaCezwM', 'Video Title 4', 6)
crud.create_youtube_record('9EhG5eU', 'Video Title 5', 14)