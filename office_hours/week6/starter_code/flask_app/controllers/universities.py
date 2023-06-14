from flask_app import app
from flask import render_template, redirect, request, session # Add other methods from Flask you might need here
# Import models here

# VISIBLE ROUTES
@app.route("/")
def universities_page():
    pass

@app.route("/universities/<int:id>")
def view_university_page(id): # Don't forget to pass in path variables!!!
    pass

# HIDDEN ROUTES
@app.route("/universities/add", methods=["POST"]) # This is a POST request route!
def add_university_to_db():
    pass

@app.route("/universities/<int:id>/delete", methods=["POST"]) # This is a POST request route!
def delete_university_from_db(id): # Don't forget to pass in path variables!!!
    pass

