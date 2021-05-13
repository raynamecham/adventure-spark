"""Server for adventure spark app."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, jsonify, flash, session, url_for, abort
from werkzeug.security import generate_password_hash, check_password_hash

from model import connect_to_db, db, User, Location, Adventure
import crud
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "adventurespark"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
@app.route('/home')
def homepage():
    """View homepage with map."""

    session['alert'] = {}
    session['alert']['type'] = None
    session['alert']['message'] = None

    locations = crud.get_locations()

    return render_template('homepage.html', locations=locations)

@app.route('/signup', methods=['POST'])
def signup():
    """User sign up """

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user('email', email)
    session['alert']['type'] = 'danger'

    if user:
        session['alert']['message'] = 'Email address already exists.'
        session['alert']['type'] = 'warning'
        return render_template('homepage.html')
    else:
        crud.create_user(name, email, password)
        session['logged_in'] = True
        session['alert']['message'] = 'Welcome to Adventure Spark, ' + name + '!'
        session['alert']['type'] = 'success'
        return render_template('homepage.html')


@app.route('/login', methods=['POST'])
def login():
    """User login"""

    email = request.form.get('email')
    password = request.form.get('password')

    current_user = User.query.filter(User.email == email, User.password == password).first()

    if not current_user:
        session['alert']['message'] = 'Email or password is incorrect.'
        session['alert']['type'] = 'danger'
        return render_template('homepage.html')

    else:
        session['logged_in'] = True
        session['alert']['type'] = None
        session['user_email'] = current_user.email
        session['user_id'] = current_user.user_id
        session['user_name'] = current_user.name

        return render_template('homepage.html')


@app.route('/logout')
def logout():
    """User logout"""
    
    session.clear()
    return redirect('/')

@app.route('/api/locations', methods=["GET"])
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


@app.route('/api/youtube_cache', methods=["GET", "POST"])
def youtube_cache():
    """Information about youtube cache"""

    if request.method == "GET":
        location_id = request.args['location_id']
        youtube_records = crud.get_youtube_records(location_id)

        return jsonify(youtube_records)

    elif request.method == "POST":
        location_id = request.form['location_id']        
        items = json.loads(request.form['items'])
        
        crud.delete_youtube_records(location_id)

        for item in items:
            crud.create_youtube_record(item['id']['videoId'], item['snippet']['title'], location_id)

        return 'success'


@app.route('/adventure_list')
def view_adventures():
    """View user's list of adventures. """

    adventure_list = crud.get_adventure_list()

    return render_template('adventure_list.html', adventure_list=adventure_list)


@app.route('/api/add_to_list', methods=["POST"])
def add_to_list():
    """Adds location name to user's adventure list"""

    if 'user_id' not in session:
        session['alert']['message'] = 'Sign up to use this feature.'
        session['alert']['type'] = 'warning'
        # TODO: reload page with alert

        return 'something'

    else:
        user_id = session['user_id']
        location_id = request.form['location_id']
        crud.create_adventure(user_id, location_id)

        session['alert']['message'] = 'Location added to your adventure list!'
        session['alert']['type'] = 'success'
        # TODO: reload page with alert

        return 'something'

if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    app.run(host="0.0.0.0")