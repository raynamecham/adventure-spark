"""Server for adventure spark app."""

from flask.helpers import url_for
from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, jsonify, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from werkzeug.security import generate_password_hash, check_password_hash

from model import connect_to_db, db, User, Location, Adventure
import crud

app = Flask(__name__)
app.config["SECRET_KEY"] = "adventurespark"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage with map."""

    return render_template('homepage.html')

@app.route('/api/homepage')
def location_info():
    """JSON information about locations."""

    locations = [
        {
            "id": location.location_id,
            "name": location.location_name,
            "latitude": location.lat,
            "longitude": location.long,
            "description": location.desc,
            "image": location.img_path
        }
        for location in Location.query.all()
    ]

    return jsonify(locations)

@app.route('/signup', methods=['POST'])
def signup():
    """User sign up """

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user(email)
    if user:
        flash('Email address already exists.')
    else:
        crud.create_user(name, email, password)
        flash('Account created! Please log in.')

    new_user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
    
    db.session.add(new_user)
    db.session.commit()

    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    """User login"""

    email = request.form.get('emaiil')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        
    return render_template('adventure_list.html')

@app.route('/logout')
def logout():
    """User logout"""

    return render_template('homepage.html')


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")