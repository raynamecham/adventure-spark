"""Script to seed database."""

import os

import crud
import model
import server

os.system('dropdb adventurespark')
os.system('createdb adventurespark')

model.connect_to_db(server.app)
model.db.create_all()




