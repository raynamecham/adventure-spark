"""Script to seed database."""

import crud
import model
import server

model.connect_to_db(server.app)

crud.create_location('Paris', 48.8620605, 2.2958039, "The City of Light draws millions of visitors every year with its unforgettable ambiance.")
crud.create_location('Bora Bora', -16.499701, -151.770538, "What this small island may lack in size it makes up for in sheer tropical beauty. Here, you'll find picturesque beaches, lush jungles and luxurious resorts.")
crud.create_location('South Island, New Zealand', -40.923859, 173.991425, "New Zealand's South Island brims with majestic landscapes at every turn, from dramatic mountains to fjords to glaciers.")
crud.create_location('Glacier National Park', 48.502281, -113.988533, "What this small island may lack in size it makes up for in sheer tropical beauty. Here, you'll find picturesque beaches, lush jungles and luxurious resorts.")

crud.create_adventure(1, 1)