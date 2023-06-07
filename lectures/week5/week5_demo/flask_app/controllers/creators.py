from flask import render_template, session, redirect, request
from flask_app import app # MAKE SURE YOU IMPORT THE app VARIABLE!!!
from flask_app.models import creator # IMPORT YOUR MODELS!

# Visible routes
@app.route("/")
def home_page():
    return render_template("login.html")

@app.route('/creators')
def all_creators_page():
    # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    print("In creators route")
    # print(request.form) # Empty - got redirected here
    # Talk to the model to grab all the content creators from the database
    all_creators = creator.Creator.get_all_creators()
    return render_template('all_creators.html', all_creators = all_creators)

@app.route("/creators/new")
def new_creator_form_page():
    # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    return render_template("add_creator.html")

# Hidden routes
@app.route("/login", methods=["POST"])
def login_user():
    session['name'] = request.form.get("name")
    return redirect("/creators")

@app.route("/logout")
def logout():
    session.clear() # Deletes all the key-value pairs from session
    return redirect("/")

# # Tip from Thomas - have a /clear route to delete session
# @app.route("/clear")
# def clear_session():
#     session.clear() # Deletes all the key-value pairs from session
#     return redirect("/")

@app.route("/creators/add", methods=["POST"])
def add_new_creator():
    # If someone isn't logged in, send user back
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    # print(request.form) # Printing off the request.form dictionary
    # NO MORE SESSION - now let's use a database!
    # Put form data (from request.form) into a new dictionary
    form_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "genre": request.form["genre"],
        "screen_name": request.form["screen_name"],
        "channel_name": request.form["channel_name"]
    }
    # Call on model to add to DB
    creator.Creator.add_creator(form_data) # file_name.ClassName.class_method_name()
    return redirect("/creators")

@app.route("/creators/<int:id>/edit")
def edit_creator_form(id): # Don't forget to pass in all your path variables!!!
    # If someone isn't logged in, send user back - added after Thursday week 4 lecture
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    data = {
        "id": id
    }
    print(data)
    this_creator = creator.Creator.get_one_creator(data)
    return render_template("edit_creator.html", this_creator = this_creator)

@app.route("/creators/<int:id>")
def view_creator_page(id):
    # If someone isn't logged in, send user back - added after Thursday week 4 lecture
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    # Need dictionary that has the ID
    data = {
        "id": id
    }
    print(data)
    # Grab Creator object by ID
    this_creator = creator.Creator.get_one_creator(data)
    return render_template("view_creator.html", this_creator = this_creator)

@app.route("/creators/<int:id>/delete", methods=["POST"])
def delete_creator_from_db(id):
    # If someone isn't logged in, send user back - added after Thursday week 4 lecture
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    # Need dictionary that has the ID
    data = {
        "id": id
    }
    creator.Creator.delete_one_creator(data)
    return redirect("/creators")

@app.route("/creators/<int:id>/edit_in_db", methods=["POST"])
def edit_creator_in_db(id):
    # If someone isn't logged in, send user back - added after Thursday week 4 lecture
    if "name" not in session:
        print("Not logged in - sending back")
        return redirect("/")
    form_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "genre": request.form["genre"],
        "screen_name": request.form["screen_name"],
        "channel_name": request.form["channel_name"],
        "id": id # DON'T FORGET YOUR ID here!!!
    }
    creator.Creator.edit_one_creator(form_data)
    return redirect(f"/creators/{id}")