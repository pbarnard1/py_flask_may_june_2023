from flask_app.config.mysqlconnection import connectToMySQL
# Import other models as needed here!

class Hall:
    db_name = "" # Fill this in!

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # We'll link a University here

    # Add other class methods here!