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
        query = """
        SELECT * FROM majors
        LEFT JOIN universities_majors
        ON majors.id = universities_majors.major_id
        LEFT JOIN universities
        ON universities.id = universities_majors.university_id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        all_major_objects = {} # Hold all UNIQUE Major objects
        # Loop through each dictionary
        for current_major_dictionary in results:
            print(current_major_dictionary)
            # If new major (ID not in dictionary called "all_major_objects")
            if str(current_major_dictionary["id"]) not in all_major_objects:
                # Create the Major object and add it to the dictionary
                major_object = cls(current_major_dictionary) # Create the new Major
                all_major_objects[str(current_major_dictionary["id"])] = major_object # Add to dictionary
            else:
                major_object = all_major_objects[str(current_major_dictionary["id"])] # Grab pre-existing Major by ID from all_major_objects dictionary
            # Create the University object
            university_data = {
                "id": current_major_dictionary["universities.id"], # Duplicate column
                "name": current_major_dictionary["universities.name"], # Duplicate column
                "city": current_major_dictionary["city"], # No "universities" needed - column is not duplicated
                "created_at": current_major_dictionary["universities.created_at"], # Duplicate column
                "updated_at": current_major_dictionary["universities.updated_at"], # Duplicate column
            }
            university_object = university.University(university_data)
            # Link this University to this Major
            major_object.universities.append(university_object)
        list_of_major_objects = all_major_objects.values() # Grabs all the Major objects as values and puts them all in a list
        return list_of_major_objects
    
    @classmethod
    def get_all_majors_not_in_university(cls, data):
        query = """
        SELECT * FROM majors 
        WHERE id NOT IN 
        (SELECT major_id FROM universities_majors 
        WHERE university_id = %(id)s);
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
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
    
    @classmethod
    def delete_major_from_university(cls, data):
        query = """
        DELETE FROM universities_majors
        WHERE university_id = %(university_id)s AND major_id = %(major_id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_major(cls, data):
        query = "DELETE FROM majors WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
