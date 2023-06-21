from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models import hall, major, university

@app.route("/majors")
def view_all_majors():
    return render_template("all_majors.html", all_majors = major.Major.get_all_majors())

@app.route('/majors/add_to_db', methods=["POST"])
def add_major_to_db():
    major.Major.add_major(request.form)
    return redirect("/majors")

@app.route('/majors/<int:id>/delete', methods=["POST"])
def delete_major_from_db(id): # Don't forget to pass in path variables!
    pass

@app.route("/majors/add_to_university", methods=["POST"])
def add_major_to_university():
    pass

@app.route("/majors/<int:major_id>/remove_from_university", methods=["POST"])
def remove_major_from_university(major_id):
    pass