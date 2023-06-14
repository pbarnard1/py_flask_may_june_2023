from flask_app.config.mysqlconnection import connectToMySQL
# Import other models as needed here!

class University:
    db_name = "" # Fill this in!

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.city = data["city"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # We'll link Halls here
        # For Thursday and next week, we'll also link Majors

    # Add other class methods here!