"""Server for adventure spark app."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, VideoLocation, Video, Location

app = Flask(__name__)
app.config["SECRET_KEY"] = "adventurespark"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route("/locations")
def view_map():
    """View map."""

    return render_template("map.html")

@app.route('/api/locations')
def location_info():
    """JSON information about locations."""

    locations = [
        {
            "id": location.location_id,
            "name": location.location_name,
            "latitude": location.lat,
            "longitude": location.long,
            "description": location.desc,
        }
        for location in Location.query.limit(30)
    ]

    return jsonify(locations)

@app.route("/videos")
def view_videos():
    """View videos."""

    return render_template("map.html")

@app.route('/api/videos')
def video_info():
    """JSON information about videos."""

    videos = [
        {
            "title": videos.title,
            "url": videos.url,
            "desc": videos.desc,
            "tag": videos.tag
        }
        for videos in Video.query.limit(30)
    ]

    return jsonify(videos)

if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")