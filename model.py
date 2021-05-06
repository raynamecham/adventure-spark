"""Models for adventure spark app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    name = db.Column(db.String, nullable=False)
    email= db.Column(db.String, unique=True, nullable=False)
    password= db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Name name={self.name} Email email={self.email} ID user_id={self.user_id}>'


class Location(db.Model):
    """A location on the map"""

    __tablename__ = 'locations'

    location_id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    location_name = db.Column(db.String, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    long = db.Column(db.Float, nullable=False)
    desc = db.Column(db.Text)
    img_path = db.Column(db.String, default='/static/img/default_image.png')


    def __repr__(self):
        return f'<Location location_id={self.location_id} location_name={self.location_name} lat={self.lat} long={self.long}>'

class Adventure(db.Model):
    """An adventure"""

    __tablename__ = 'adventures'

    id = db.Column(db.Integer,
                    autoincrement=True,
                    primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.location_id'), nullable=False)
    visited = db.Column(db.Boolean, default=False, nullable=False)

    user = db.relationship('User', backref='adventures')
    location = db.relationship('Location', backref='adventures')

    def __repr__(self):
        return f'<User user_id={self.user_id} Location location_id={self.location_id}>'


def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adventurespark'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)
    print("Connected to DB.")


