from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "mysecretflaskkey" # Need this for session (and other stuff later on)

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
    return render_template('all_creators.html')

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
    # TEMPORARY FOR THIS LECTURE ONLY (and for this week's core assignments) - Saving form values in session
    session['first_name'] = request.form.get("first_name")
    session['last_name'] = request.form.get("last_name")
    session['screen_name'] = request.form.get("screen_name")
    session['genre'] = request.form.get("genre")
    session['channel_name'] = request.form.get("channel_name")
    print(request.form) # Printing off the request.form dictionary
    return redirect("/creators")

if __name__ == "__main__":
    app.run(debug=True)