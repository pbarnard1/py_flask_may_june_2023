from flask import Flask, render_template # Need to import render_template to serve HTML files
app = Flask(__name__)

@app.route("/")
def home_route():
    return render_template("first_page.html") # Return a file called "first_page.html"

@app.route("/demo/<name>/<int:number>")
def passing_values_demo_page(name, number): # Remember to pass in ALL path variables as parameters!!
    list_of_teachers = ["Adrian","Lee","Melissa","Nathan","Melinda","Jennifer"]
    # Notice how we're passing values - it's always variable_name_to_use_in_HTML = value_assigned
    # We have access to user_name, number and list_of_teachers in the HTML - all of these variables come before the "=" sign
    return render_template("passing_values_demo.html", user_name = name, number = number, list_of_teachers = list_of_teachers)

if __name__=="__main__":
    app.run(debug=True)