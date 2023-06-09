from flask_app.config.mysqlconnection import connectToMySQL

class Athlete:
    db = "" # Put your schema name here!

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.sport = data["sport"]
        self.birthdate = data["birthdate"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # You will write your class methods here to add an athlete to the database and grab all athletes!
