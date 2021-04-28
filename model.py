"""Models for adventure spark app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class VideoLocation(db.Model):
    """Video of a specific location."""

    ___tablename___= 'videos_locations'

    video_location_id = db.Column(db.Integer,
                                autoincrement=True,
                                primary_key=True)
    location_id = db.Column(db.Integer,
                            db.ForeignKey('locations.location_id'),
                            nullable=False)
    video_id = db.Column(db.Integer,
                        db.ForeignKey('videos.video_id'),
                        nullable=False)

    location = db.relationship("Location", backref="locations")
    video = db.relationship("Video", backref="videos")

    def __repr__(self):
        return "<VideoLocation location_id={} video_id={}>".format(self.location_id, self.video_id)


class Video(db.Model):
    """A video"""

    __tablename__ = 'videos'

    video_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    desc = db.Column(db.String)
    tag = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Video video_id={self.video_id} title={self.title}> '

class Location(db.Model):
    """A location on the map"""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    location_name = db.Column(db.String, nullable=False)
    lat = db.Column(db.Integer, nullable=False)
    long = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String)

    def __repr__(self):
        return f'<Location location_id={self.location_id} location_name={self.location_name} lat={self.lat} long={self.long}>'


def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///locations'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")


