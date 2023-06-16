from flask_app.config.mysqlconnection import connectToMySQL
# Import other models as needed here!
from flask_app.models import university

class Hall:
    db_name = "universities_schema" # Fill this in!

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # We'll link a University here
        self.university = None # Linking ONE University

    # Add other class methods here!
    @classmethod
    def add_one_hall(cls, data):
        query = """
        INSERT INTO halls
        (name, university_id)
        VALUES
        (%(name)s, %(university_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_halls_with_universities(cls):
        query = """
        SELECT * FROM halls
        JOIN universities
        ON universities.id = halls.university_id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        hall_object_list = [] # Hold a bunch of Hall objects
        # Grab each dictionary from the list
        for hall_dictionary in results:
            print(hall_dictionary)
            # Create the Hall object
            new_hall_object = cls(hall_dictionary)
            # Create the University object
            university_data = {
                "id": hall_dictionary["universities.id"], # Duplicate column name, so add name of table we're joining with
                "name": hall_dictionary["universities.name"],
                "city": hall_dictionary["city"],
                "created_at": hall_dictionary["universities.created_at"],
                "updated_at": hall_dictionary["universities.updated_at"],
            }
            new_university_object = university.University(university_data)
            # Link the University and Hall objects together
            new_hall_object.university = new_university_object
            # Add this Hall to the list
            hall_object_list.append(new_hall_object)
        return hall_object_list # WATCH YOUR INDENTATION!