from flask import Flask # Import Flask class
app = Flask(__name__) # Create app variable

# Define some routes
@app.route('/') # ALL routes start with a "/"
def root_route():
    return "Hello!  This is our first Flask response!" 

@app.route("/myblog")
def blog_page():
    return "This is a very short blog from Adrian!"

@app.route("/myblog/<blog_id>") # Now using a variable rule (aka a "path variable") called "blog_id"
def blog_page_number(blog_id): # All variable rules MUST be passed in as parameters!!!!
    return f"This is blog number {blog_id} from Adrian!"

@app.route("/myblog/<blog_id>/<name>") # 2 path variables: blog_id and name
def blog_page_number_and_name(blog_id, name): # Pass in both variable rules
    return f"This is blog number {blog_id} from {name}!"

# To be answered tomorrow: What data types are blog_id and name (e.g. number, string, list, something else)?  
# Can we use different data types instead?

if __name__=="__main__": # To run the app
    app.run(debug=True) # If you're a Mac user, you might need a different port number (see platform)