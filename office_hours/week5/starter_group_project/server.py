from flask_app import app
from flask_app.controllers import athletes # Make sure you import ALL controllers!

if __name__=="__main__":
    app.run(debug=True) # Add port number if needed ", port=8000" (for port 8000)