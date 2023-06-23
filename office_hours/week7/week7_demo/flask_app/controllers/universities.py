from flask_app import app
from flask import render_template, redirect, request, session # Add other methods from Flask you might need here
# Import models here
from flask_app.models import university, hall, major

# VISIBLE ROUTES
@app.route("/")
def universities_page():
    return render_template("all_universities.html", all_universities = university.University.get_all_universities())

@app.route("/universities/<int:id>")
def view_university_page(id): # Don't forget to pass in path variables!!!
    data = {
        "id": id,
    }
    return render_template("view_university.html", 
        this_university = university.University.get_one_university_with_halls_and_majors(data),
        all_majors = major.Major.get_all_majors())

# HIDDEN ROUTES
@app.route("/universities/add", methods=["POST"]) # This is a POST request route!
def add_university_to_db():
    university.University.add_university(request.form)
    return redirect("/")

@app.route("/universities/<int:id>/delete", methods=["POST"]) # This is a POST request route!
def delete_university_from_db(id): # Don't forget to pass in path variables!!!
    data = {
        "id": id
    }
    university.University.delete_university(data)
    return redirect("/")

