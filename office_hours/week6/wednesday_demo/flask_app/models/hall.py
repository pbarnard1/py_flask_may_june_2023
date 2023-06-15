from flask_app.config.mysqlconnection import connectToMySQL
# Import other models as needed here!

class Hall:
    db_name = "universities_schema" # Fill this in!

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # We'll link a University here

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
        # We'll finish this Thursday