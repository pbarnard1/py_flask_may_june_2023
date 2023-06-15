from flask_app.config.mysqlconnection import connectToMySQL
# Import other models as needed here!

class University:
    db_name = "universities_schema" # Fill this in!

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.city = data["city"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # We'll link Halls here
        # For Thursday and next week, we'll also link Majors

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