# """CRUD operations."""

from model import db, User, Location, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_location(location_name, lat, long, desc, search_key):
    """Create and return a new location on the map."""

    location = Location(location_name=location_name,
                        lat=lat,
                        long=long,
                        desc=desc,
                        search_key=search_key)

    db.session.add(location)
    db.session.commit()

    return location

if __name__ == '__main__':
    from server import app
    connect_to_db(app)




