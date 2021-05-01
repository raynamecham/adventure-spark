"""Script to seed database."""

import os

import crud
import model
import server

os.system('dropdb adventurespark')
os.system('createdb adventurespark')

model.connect_to_db(server.app)
model.db.create_all()

crud.create_user('Rayna', 'rayna.mecham@gmail.com', 'admin')

crud.create_location('Paris', 48.8620605, 2.2958039, "The City of Light draws millions of visitors every year with its unforgettable ambiance.")
crud.create_location('Bora Bora', -16.499701, -151.770538, "What this small island may lack in size it makes up for in sheer tropical beauty. Here, you'll find picturesque beaches, lush jungles and luxurious resorts.")

crud.create_adventure(1, 1)