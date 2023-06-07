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
    return render_template("all_contents.html")





@app.route("/contents/<int:id>")
def view_content_page(id):
        # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    return render_template("view_content.html")

@app.route("/contents/<int:id>/edit")
def edit_content_page(id):
        # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    return render_template("edit_content.html")

# Hidden route
@app.route("/contents/add_to_db", methods=["POST"])
def add_content_to_db():
    # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    new_content_id = content.Content.add_content(request.form) # Talk to model to add to DB
    return redirect(f"/contents/{new_content_id}") # Redirect to new content page's route

@app.route("/contents/<int:id>/delete", methods=["POST"])
def delete_from_db(id):
        # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    pass

@app.route("/contents/<int:id>/edit_in_db", methods=["POST"])
def edit_content_in_db(id):
        # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    pass
