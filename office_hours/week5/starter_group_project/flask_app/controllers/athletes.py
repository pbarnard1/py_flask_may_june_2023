from flask import render_template, request, session, redirect
from flask_app import app

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
    return render_template("all_athletes.html")

# What other routes will you need?