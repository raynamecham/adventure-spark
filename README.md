# Adventure Spark

>"So much of who we are is where we have been."
-William Langewiesche



![Python Versions](https://img.shields.io/pypi/pyversions/yt2mp3.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/raynamecham/adventure-spark)
![GitHub language count](https://img.shields.io/github/languages/count/raynamecham/adventure-spark)

## Table of Contents

1. - [Overview](#overview)
2. - [Technologies](#technologies)
3. - [Installation](#installation)
4. - [Roadmap](#roadmap)
5. - [About the developer](#about-the-developer)

### Overview
<a name="Overview"></a>

I wanted to be able to utilize two APIs in a very unique way. Adventure Spark does just that! Users are able to see points of interest on a world map using the Google Maps API, scroll around the map, and click on the map markers. Clicking on the points will make a call to the YouTube API and display a list of videos of things to do in that city. Users are able to do a quick search for points on the map as well. Users can also keep a personal list of places they have visited and want to visit in the future on an adventure "bucket list".

Check out the live site at https://adventure-spark.fun

***Any user can see the world map and location markers.***

![](/demo/adventurespark1.gif)

***They can click on a marker and the videos about that location will auto populate.***

![](/demo/adventurespark2.gif)

***To add an adventure to your list, you must sign up and log in.***

![](/demo/adventurespark3.gif)

![](/demo/adventurespark4.gif)

***Logged in users can add, check off, and remove adventures from their list.***

![](/demo/adventurespark5.gif)


### Technologies

<a name="Technologies"></a>
- Python, SQLAlchemy, PostgreSQL, Flask, Bcrypt, Selenium
- Javascript, jQuery(AJAX, JSON), Jinja2, Bootstrap 4, Google Fonts, HTML5, CSS3
- APIs: Google Maps with Places library, YouTube


### Installation

<a name="installation"></a>
Tip: Create your own virtual environment to run this project.
***
Run these commands to install and run. 
```
$ git clone https://github.com/raynamecham/adventure-spark
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ python3 server.py
```

### Roadmap

<a name="Roadmap"></a>
Future releases:
- User will be able to add their own map marker locations
- Save videos to personal adventure list to watch later
- User uploaded photos of adventures

### About the developer

<a name="about-the-developer"></a>
Originally from Washington, Rayna now resides in Utah with her husband and 3 kids. She has been a stay-at-home parent while her kids were little and loves being a mom. Now that her kids are older, she is pursuing a full-time career in frontend software development. She loves reading, music, trying out new recipes, and traveling. Rayna has always prided herself on being knowledgeable with tech amongst family and friends. The last several years brought about opportunities to learn web development in a freelance format, which caused her to think this might be what she'd like to do for a career. After making several websites for clients, she decided to amp up her skills and join Hackbright! Adventure Spark is her capstone project. Find her on [LinkedIn](https://www.linkedin.com/in/rayna-mecham/) and on [Github](https://github.com/raynamecham).
