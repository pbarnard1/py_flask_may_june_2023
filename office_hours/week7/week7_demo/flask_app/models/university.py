from flask_app.config.mysqlconnection import connectToMySQL
# Import other models as needed here!
from flask_app.models import hall, major

class University:
    db_name = "universities_schema" # Fill this in!

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.city = data["city"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # We'll link Halls here
        self.halls = [] # Link MANY Halls
        self.majors = [] # Link MANY Majors

    # Add other class methods here!
    @classmethod
    def add_university(cls, data): # Don't forget to start with "cls" for all class methods!
        query = """
        INSERT INTO universities
        (name, city)
        VALUES
        (%(name)s, %(city)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all_universities(cls): # No data needed - no values to put in query
        query = "SELECT * FROM universities;"
        results = connectToMySQL(cls.db_name).query_db(query)
        # List of University objects
        all_university_objects = []
        # Go through each university's data from our results
        # and then create the University object, which will
        # be added to our list
        for each_university_dictionary in results:
            print(each_university_dictionary)
            # Create the University object
            new_university_object = cls(each_university_dictionary) # same as University()
            # Add this University to the list
            all_university_objects.append(new_university_object)
        return all_university_objects
    
    @classmethod
    def get_one_university_with_halls(cls, data):
        query = """
        SELECT * FROM universities
        LEFT JOIN halls
        ON universities.id = halls.university_id
        WHERE universities.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results) # LIST
        # print(results[0]) # DICTIONARY at index 0 in the list
        # Create the University object
        university_dictionary = results[0] # Grab the first item as that's guaranteed to be found, assuming that university exists
        university_object = cls(university_dictionary) # This is essentially University()
        # Go through each hall
        for each_hall_dictionary in results:
            # To prevent us from creating a Hall object if no data found
            if each_hall_dictionary["halls.id"] == None:
                break
            print(each_hall_dictionary)
            # Create each Hall object, then link it to the University object
            hall_info = {
                "id": each_hall_dictionary["halls.id"], # Duplicate column name, so table name added
                "name": each_hall_dictionary["halls.name"], # Duplicate column name, so table name added
                "created_at": each_hall_dictionary["halls.created_at"], # Duplicate column name, so table name added
                "updated_at": each_hall_dictionary["halls.updated_at"], # Duplicate column name, so table name added
            }
            hall_object = hall.Hall(hall_info)
            # Link this Hall to the list of halls for this University
            university_object.halls.append(hall_object)
        return university_object
    
    @classmethod
    def get_one_university_with_halls_and_majors(cls, data):
        query = """
        SELECT * FROM universities
        LEFT JOIN universities_majors
        ON universities.id = universities_majors.university_id
        LEFT JOIN majors
        ON majors.id = universities_majors.major_id
        LEFT JOIN halls
        ON halls.university_id = universities.id
        WHERE universities.id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results) # LIST
        # print(results[0]) # DICTIONARY at index 0 in the list
        # Create the University object
        university_dictionary = results[0] # Grab the first item as that's guaranteed to be found, assuming that university exists
        university_object = cls(university_dictionary) # This is essentially University()
        held_hall_objects = {} # Dictionary holding unique Halls
        # Go through each hall
        for each_hall_dictionary in results:
            print(each_hall_dictionary)
            # To prevent us from creating a Hall object if no data found
            if each_hall_dictionary["halls.id"] == None:
                break
            if str(each_hall_dictionary["halls.id"]) not in held_hall_objects:
                # Create each Hall object, then link it to the University object
                hall_info = {
                    "id": each_hall_dictionary["halls.id"], # Duplicate column name, so table name added
                    "name": each_hall_dictionary["halls.name"], # Duplicate column name, so table name added
                    "created_at": each_hall_dictionary["halls.created_at"], # Duplicate column name, so table name added
                    "updated_at": each_hall_dictionary["halls.updated_at"], # Duplicate column name, so table name added
                }
                hall_object = hall.Hall(hall_info)
                # Link this Hall to the list of halls for this University
                university_object.halls.append(hall_object)
                held_hall_objects[str(each_hall_dictionary["halls.id"])] = hall_object
        # New dictionary that will hold Major objects so we don't duplicate them
        held_major_objects = {}
        # Go through each major
        for each_major_dictionary in results:
            # If no Major linked to university, don't both looping, as there are no Majors to create
            if each_major_dictionary["majors.id"] == None:
                break
            # Check to see if we already created the Major object
            if str(each_major_dictionary["majors.id"]) not in held_major_objects:
                
                major_info = {
                    "id": each_major_dictionary["majors.id"],
                    "name": each_major_dictionary["majors.name"],
                    "created_at": each_major_dictionary["majors.created_at"],
                    "updated_at": each_major_dictionary["majors.updated_at"],
                }
                # Make the Major object
                major_object = major.Major(major_info)
                held_major_objects[str(each_major_dictionary["majors.id"])] = major_object
                # Link this Major to this University
                university_object.majors.append(major_object)
        return university_object

    @classmethod
    def delete_university(cls, data):
        query = "DELETE FROM universities WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
