# """CRUD operations."""

from flask import Flask
from flask_bcrypt import Bcrypt
from flask.globals import session
from model import db, User, Location, Adventure, YouTubeCache, connect_to_db
from datetime import datetime, timedelta

app = Flask(__name__)
bcrypt = Bcrypt(app)

#User functions

def create_user(name, email, password):
    """Create and return a new user."""

    password = bcrypt.generate_password_hash(password).decode('utf-8')

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
    elif (param_type == "user_id"):
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

def get_adventures(user_id = 0):
    """Get an adventure by id."""

    adventures = db.session.query(Adventure, Location).filter_by(user_id = session['user_id']).join(Location).all()
    return adventures

def delete_adventure(adventure_id):
    """Delete an adventure"""

    adventure = Adventure.query.get(adventure_id)

    db.session.delete(adventure)
    db.session.commit()

def update_adventure(adventure_id, visited):
    """Update adventure visited info"""

    # Convert string to bool
    if visited == "False":
        visited = False
    else:
        visited = True

    result = Adventure.query.filter(Adventure.adventure_id == adventure_id).update({Adventure.visited: visited})
    db.session.commit()
    return result
    
# YouTubeCache functions

def create_youtube_record(video_id, video_title, location_id):
    """Create new youtube record"""

    youtube_record = YouTubeCache(video_id=video_id, video_title=video_title, location_id=location_id)

    db.session.add(youtube_record)
    db.session.commit()

def get_youtube_records(location_id):
    """Return all youtube records."""

    twentyFourHoursAgo = datetime.now() - timedelta(hours = 24)

    youtube_records = [
        {
            "snippet": {
                "title": youtube_record.video_title
            },
            "id": {
                "videoId": youtube_record.video_id
            }
        }
        for youtube_record in YouTubeCache.query.filter(YouTubeCache.location_id == location_id, YouTubeCache.fetched > twentyFourHoursAgo).limit(3).all()
    ]
    
    return {"items": youtube_records}


def delete_youtube_records(location_id):
    """Delete an adventure"""

    num_rows_deleted = YouTubeCache.query.filter(YouTubeCache.location_id == location_id).delete()

    db.session.commit()
    return num_rows_deleted

if __name__ == '__main__':
    from server import app
    connect_to_db(app)




