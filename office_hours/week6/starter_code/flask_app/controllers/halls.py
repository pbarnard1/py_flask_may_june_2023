from flask_app import app
from flask import render_template, redirect, request, session # Add other methods from Flask you might need here
# Import models here

# VISIBLE ROUTES
@app.route("/halls")
def halls_page():
    pass

@app.route("/halls/<int:id>/edit")
def edit_hall_page(id): # Don't forget to pass in path variables!!!
    pass

# HIDDEN ROUTES
@app.route("/halls/add", methods=["POST"]) # This is a POST request route!
def add_hall_to_db():
    pass

@app.route("/halls/<int:id>/edit_in_db", methods=["POST"]) # This is a POST request route!
def edit_hall_in_db(id): # Don't forget to pass in path variables!!!
    pass

@app.route("/halls/<int:id>/delete", methods=["POST"]) # This is a POST request route!
def delete_hall_from_db(id): # Don't forget to pass in path variables!!!
    pass