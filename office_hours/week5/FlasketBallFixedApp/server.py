from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "unicorns"


@app.route('/') 
def index():

    return render_template("index.html", )

@app.route('/leaderboard')
def leaderBoard():
    return render_template("leaderboard.html")

# Bug fix: forcing rank to be an integer data type instead of a string by default
@app.route('/show/<int:rank>') # If you don't specify the type, a path variable will default to a string data type
def show(rank):
    print(rank)
    print(type(rank))
    if rank == 1: 
        name = session['first']
    elif rank == 2:
        name = session['second']
    else:
        name = session['third']

    return render_template("showFriend.html", rank=rank, name=name)

@app.route('/enter', methods = ['POST'])
def enter():
    print(request.form)
    name = request.form["firstName"] + " " + request.form["lastName"]
    session['user_name'] = name
    return redirect('/leaderboard')

@app.route("/changeRanks", methods=["POST"]) # Mention that this is a POST request
def changeRanks():
    # Bug fix: saved these in session to make them available all across the app
    session["first"] = request.form['first']
    session["second"] = request.form['second']
    session["third"] = request.form['third']
    # Bug fix: NEVER pass values along when you redirect!  Only
    # mention the route name you're going to!
    return redirect('/leaderboard')

    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)