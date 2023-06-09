from flask import render_template, session, redirect, request
from flask_app import app # MAKE SURE YOU IMPORT THE app VARIABLE!!!
from flask_app.models import content, creator # IMPORT YOUR MODELS!

@app.route("/contents/new")
def new_content_page():
    # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    return render_template("add_content.html", all_content_creators = creator.Creator.get_all_creators())

@app.route("/contents")
def all_content_page():
    # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    return render_template("all_contents.html", contents = content.Content.get_all_content())


@app.route("/contents/<int:id>")
def view_content_page(id):
        # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    # Need dictionary as that will hold a specific ID
    data_dictionary = {"id": id}
    return render_template("view_content.html", this_post = content.Content.get_one_post(data_dictionary))

@app.route("/contents/<int:id>/edit")
def edit_content_page(id):
        # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    data_dictionary = {"id": id}
    return render_template("edit_content.html", 
        this_post = content.Content.get_one_post(data_dictionary),
        all_content_creators = creator.Creator.get_all_creators())

# Hidden route
@app.route("/contents/add_to_db", methods=["POST"])
def add_content_to_db():
    # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    if not content.Content.validate_content(request.form): # If validations are no good
        return redirect("/contents/new") # NOTE: Redirect to correct route - the last route you were on that has the form
    new_content_id = content.Content.add_content(request.form) # Talk to model to add to DB
    return redirect(f"/contents/{new_content_id}") # Redirect to new content page's route

@app.route("/contents/<int:id>/delete", methods=["POST"])
def delete_from_db(id):
        # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    data_dictionary = {"id": id}
    content.Content.delete_content(data_dictionary)
    return redirect("/contents")

@app.route("/contents/<int:id>/edit_in_db", methods=["POST"])
def edit_content_in_db(id):
        # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    if not content.Content.validate_content(request.form):
        return redirect(f"/contents/{id}/edit") # NOTE: Redirect to correct route - the last route you were on that has the form
    content.Content.edit_content(request.form) # Call on model to talk to DB to edit
    return redirect(f"/contents/{id}") # Go back to that content's page
