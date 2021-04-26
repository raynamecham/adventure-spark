"""Models for adventure spark app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.Text)

    def __repr__(self):
        return f'<User user_id={self.user_id}>'

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
    search_key = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Location location_id={self.location_id} location_name={self.location_name} lat={self.lat} long={self.long}>'

# class Video(db.Model):
#     """A video"""

#     __tablename__ = 'videos'

#     video_id = db.Column(db.Integer,
#                         autoincrement=True,
#                         primary_key=True)
#     title = db.Column(db.String, nullable=False)
#     url = db.Column(db.String, nullable=False)
#     desc = db.Column(db.String)
#     search_key = db.Column(db.String, db.ForeignKey('locations.search_key'), nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

#     location = db.relationship('Location', backref='videos')
#     user = db.relationship('User', backref='videos')

#     def __repr__(self):
#         return f'<Video video_id={self.video_id} title={self.title}> '

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


