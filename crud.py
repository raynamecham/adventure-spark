# """CRUD operations."""

from model import db, VideoLocation, Video, Location, connect_to_db

def create_location(location_name, lat, long, desc):
    """Create and return a new location on the map."""

    location = Location(location_name=location_name,
                        lat=lat,
                        long=long,
                        desc=desc)

    db.session.add(location)
    db.session.commit()

    return location

def create_video(title, url, desc, tag):
    """Create and return a new video."""

    video = Video(title=title,
                url=url,
                desc=desc,
                tag=tag)

    db.session.add(video)
    db.session.commit()

    return video

if __name__ == '__main__':
    from server import app
    connect_to_db(app)




