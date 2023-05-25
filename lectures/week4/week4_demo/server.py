from flask_app import app # don't forget the app!
from flask_app.controllers import creators # IMPORT *ALL* your controllers!!!!

if __name__=="__main__":
    app.run(debug=True)