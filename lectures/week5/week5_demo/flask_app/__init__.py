from flask import Flask
app = Flask(__name__)
app.secret_key = "mysecrettoeverybody" # For session among other uses