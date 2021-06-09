"""Server for adventure spark app."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, redirect, jsonify, session, abort
from flask_bcrypt import Bcrypt


from model import connect_to_db, db, User, Location, Adventure
import crud
import json

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config["SECRET_KEY"] = "adventurespark"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
@app.route('/home')
def homepage():
    """View homepage with map."""
    
    if 'alert' not in session:
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

    # hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


    user = crud.get_user('email', email)
    session['alert']['type'] = 'danger'

    if user:
        session['alert']['message'] = 'Email address already exists.'
        session['alert']['type'] = 'warning'
        return render_template('homepage.html')
    else:
        crud.create_user(name, email, password)

        current_user = User.query.filter(User.email == email, User.password == password).first()

        session['logged_in'] = True
        session['user_email'] = current_user.email
        session['user_id'] = current_user.user_id
        session['user_name'] = current_user.name
        
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

        return redirect('/')


@app.route('/logout')
def logout():
    """User logout"""
    
    session.clear()
    return redirect('/')

@app.route('/sign_me_up')
def view_sign_up():
    """View sign up page"""

    return render_template('sign_up.html')


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
    """JSON information about youtube cache"""

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
    """View user's list of adventures, list and map."""

    adventures = crud.get_adventures(session['user_id'])

    return render_template('adventure_list.html', adventures=adventures, map=map)


@app.route('/api/add_to_list', methods=["POST"])
def add_to_list():
    """Adds location name to user's adventure list, this creates an 'adventure'."""

    if 'user_id' not in session:
        abort(500)
        
    user_id = session['user_id']
    location_id = request.form['location_id']
    crud.create_adventure(user_id, location_id)

    return 'success'

@app.route('/api/delete_adventure', methods=["POST"])
def delete_adventure():
    """Deletes an adventure off user's Adventure List"""

    adventure_id = request.form.get('adventure_id')

    if 'user_id' not in session:
        abort(500)

    crud.delete_adventure(adventure_id)

    return 'success'

@app.route('/api/update_adventure', methods=["POST"])
def update_adventure():
    """Updates user's visited list locations to True"""

    adventure_id = request.form.get('adventure_id')
    visited = request.form.get('visited')

    if 'user_id' not in session:
        abort(500)
    
    result = crud.update_adventure(adventure_id, visited)
    print(result)

    return 'success'


if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    app.run(host="0.0.0.0")