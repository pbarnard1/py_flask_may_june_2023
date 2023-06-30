from flask import Flask, render_template, jsonify, request
app = Flask(__name__)
import requests

@app.route("/")
def main_page():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_api():
    # Grab our form data
    print(request.form)
    lower_case_name = request.form["name"].lower() # Makes the entry lower case for the API to work
    api_response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{lower_case_name}")
    print(api_response)
    # print(api_response.json()) # Show raw JSON data
    return jsonify(api_response.json())

if __name__=="__main__":
    app.run(debug=True)