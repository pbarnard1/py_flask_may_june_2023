from flask_app import app
from flask import render_template, redirect, request, session # Add other methods from Flask you might need here
# Import models here
from flask_app.models import hall, university

# VISIBLE ROUTES
@app.route("/halls")
def halls_page():
    return render_template("all_halls.html", 
        all_halls = hall.Hall.get_all_halls_with_universities(),
        all_universities = university.University.get_all_universities())

@app.route("/halls/<int:id>/edit")
def edit_hall_page(id): # Don't forget to pass in path variables!!!
    pass

# HIDDEN ROUTES
@app.route("/halls/add", methods=["POST"]) # This is a POST request route!
def add_hall_to_db():
    hall.Hall.add_one_hall(request.form)
    return redirect("/halls")

@app.route("/halls/<int:id>/edit_in_db", methods=["POST"]) # This is a POST request route!
def edit_hall_in_db(id): # Don't forget to pass in path variables!!!
    pass

@app.route("/halls/<int:id>/delete", methods=["POST"]) # This is a POST request route!
def delete_hall_from_db(id): # Don't forget to pass in path variables!!!
    pass