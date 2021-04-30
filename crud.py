# """CRUD operations."""

from model import db, User, Location, Adventure, connect_to_db



#User functions

def create_user(name, email, password):
    """Create and return a new user."""

    user = User(name=name, email=email, password=password)

    db.session.add(user)
    db.session.commit()

def get_users():
    """Return all users"""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by id"""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

# def update_user():
#     """Update user info."""

def delete_user(user_id):
    """Delete user."""

    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()



#Location functions

def create_location(location_name, lat, long, desc):
    """Create and return a new location on the map."""

    location = Location(location_name=location_name,
                        lat=lat,
                        long=long,
                        desc=desc)

    db.session.add(location)
    db.session.commit()

    return location

def get_locations():
    """Return all locations."""

    return Location.query.all()

def get_location_by_name(location_name):
    """Return a location by name."""

    return Location.query.get(location_name)

# def update_location():
#     """Update location info."""

def delete_location(location_name):
    """Delete a location by name."""

    location = Location.query.get(location_name)

    db.session.delete(location)
    db.session.commit()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)




