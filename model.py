"""Models for adventure spark app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    def __repr__(self):
        return f'<User user_id={self.user_id}>'

class Map(db.Model):
    """A location on the map"""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    lat = db.Column(db.Integer, nullable=False)
    long = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String)
    search_key = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Location location_id={self.location_id} name={self.name} \
                address={self.address} lat={self.lat} long={self.long}>'

class Video(db.Model):
    """A video"""

    __tablename__ = 'videos'

    video_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    desc = db.Column(db.String)
    search_key = db.Column(db.String, db.ForeignKey('locations.search_key'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    location = db.relationship('Location', backref='videos')
    user = db.relationship('User', backref='videos')

    def __repr__(self):
        return f'<Video video_id={self.video_id} title={self.title}> '

def connect_to_db(flask_app, db_uri='postgresql:///locations', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    # connect_to_db(app, echo=False) 
    
    connect_to_db(app)

