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

def get_user(param_type, param):
    """Return user by email or id"""

    if (param_type == "email"):
        return User.query.filter(User.email == param).first()
    elif (param_type == "id"):
        return User.query.get(param)

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

def get_location(location_id):
    """Return a location by id."""

    return Location.query.get(location_id)


# def update_location():
#     """Update location info."""

def delete_location(location_id):
    """Delete a location by name."""

    location = Location.query.get(location_id)

    db.session.delete(location)
    db.session.commit()


# Adventure functions

def create_adventure(user_id, location_id):
    """Create new adventure"""

    adventure = Adventure(user_id=user_id, location_id=location_id)

    db.session.add(adventure)
    db.session.commit()

def get_adventure_list():
    """Get an adventure by id."""

    adventure_list = Location.query.join('adventures').all()

    return adventure_list

def get_adventures(user_id = 0):
    """Return all adventures by a user if id is given.
        Otherwise, return all adventures."""

    if user_id == 0:
        return Adventure.query.all()
    else: 
        return Adventure.query.get(user_id)

def delete_adventure(id):
    """Delete an adventure"""

    adventure = Adventure.query.get(id)

    db.session.delete(adventure)
    db.session.commit()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)




