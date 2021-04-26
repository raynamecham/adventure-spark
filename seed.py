"""Load location data into database."""

from model import Location, connect_to_db, db
from server import app

#---------------------------------------------------------------------#

def get_locations():
    """Load locations from dataset into database."""

    with open("data/locations.json") as location_data:
        for i, row in enumerate(location_data):
            if i >= 50:
                break

            db.session.add(Location(*row.rstrip().split(",")))

            if i % 10 == 0:
                print("{i} locations have been added to the database".format(i=i))

    db.session.commit()

#---------------------------------------------------------------------#

if __name__ == '__main__':
    connect_to_db(app)
    db.create_all()

    get_locations()