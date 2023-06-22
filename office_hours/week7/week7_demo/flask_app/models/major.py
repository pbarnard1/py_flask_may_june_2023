from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import hall, university

class Major:
    db_name = "universities_schema" # Fill this in!

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.universities = [] # List of MANY University objects linked to this Major

    @classmethod
    def add_major(cls, data):
        query = """
        INSERT INTO majors
        (name)
        VALUES
        (%(name)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_majors(cls):
        query = "SELECT * FROM majors;"
        results = connectToMySQL(cls.db_name).query_db(query)
        list_of_major_objects = []
        # Loop through each dictionary
        for current_major_dictionary in results:
            print(current_major_dictionary)
            new_major_object = cls(current_major_dictionary)
            list_of_major_objects.append(new_major_object)
        return list_of_major_objects # Make sure this return statement is NOT in the for loop
    
    @classmethod
    def add_major_to_university(cls, data):
        query = """
        INSERT INTO universities_majors
        (university_id, major_id)
        VALUES
        (%(university_id)s, %(major_id)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
