from flask import Flask, request, redirect, session, flash, render_template
app = Flask(__name__)
app.secret_key = "unicorns"


@app.route('/') 
def index():

    return render_template("index.html", )

@app.route('/leaderboard')
def leaderBoard():

    return render_template("leaderboard.html")



@app.route('/show/<rank>')
def show(rank):

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



@app.route("/changeRanks")
def changeRanks():

    first = request.form['first']
    second = request.form['second']
    third = request.form['third']

    return redirect('/leaderboard', first=first, second=second, third=third)

    

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)