from flask_app.config.mysqlconnection import connectToMySQL

class Athlete:
    db = "athletes_schema_jun_2023" # Put your schema name here!

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
    @classmethod
    def add_athlete(cls, data):
        query = """
        INSERT INTO athletes
        (first_name, last_name, sport, birthdate, description)
        VALUES
        (%(first_name)s, %(last_name)s, %(sport)s, %(birthdate)s, %(description)s); 
        """ # Remember to include the %(column_name)s for each name at the end
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_athletes(cls):
        query = "SELECT * FROM athletes;"
        results = connectToMySQL(cls.db).query_db(query)
        list_of_athlete_objects = [] # Hold a bunch of Athlete objects
        # Loop through each dictionary in the list
        for this_athlete_dictionary in results:
            print(this_athlete_dictionary)
            new_athlete_object = cls(this_athlete_dictionary) # cls() calls on the init method in this class - so think of it in this case as Athlete()
            list_of_athlete_objects.append(new_athlete_object) # Add Athlete object to list
        return list_of_athlete_objects # Return this list of Athlete objects