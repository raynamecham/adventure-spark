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
    location_name, lat, long, desc = (location['location_name'],
                                    location['lat'],
                                    location['long'],
                                    location['desc'])

    db_location = crud.create_location(location_name, lat, long, desc)
    locations_in_db.append(db_location)


with open('data/videos.json') as f:
    video_data = json.loads(f.read())


videos_in_db = []
for video in video_data:
    title, url, desc, tag  = (video['title'],
                            video['url'],
                            video['desc'],
                            video['tag'])

    db_video = crud.create_video(title, url, desc, tag)
    locations_in_db.append(db_video)