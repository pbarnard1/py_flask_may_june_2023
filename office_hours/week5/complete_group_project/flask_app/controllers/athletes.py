from flask import render_template, request, session, redirect
from flask_app import app
from flask_app.models import athlete
# from flask_app.models.athlete import Athlete

@app.route("/")
def root_route():
    return redirect("/athletes/new")

# Route that shows the new athlete form
@app.route("/athletes/new")
def add_athlete_form():
    return render_template("add_athlete.html")

# All athletes page
@app.route("/athletes")
def all_athletes_page():
    return render_template("all_athletes.html", all_athletes = athlete.Athlete.get_all_athletes())

@app.route('/athletes/add_to_db', methods=["POST"]) # Route to process the route
def add_athlete_to_db():
    print(request.form)
    athlete.Athlete.add_athlete(request.form)
    # Athlete.add_athlete(request.form)
    return redirect("/athletes") # Always redirect with a POST route

# What other routes will you need?