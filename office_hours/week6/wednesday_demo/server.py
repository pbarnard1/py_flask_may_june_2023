from flask_app import app
from flask_app.controllers import halls, universities # Import ALL your controllers

if __name__=="__main__":
    app.run(debug=True)