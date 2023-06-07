from flask_app.config.mysqlconnection import connectToMySQL # Remember to import this for all your models so we can talk to DB

class Creator:
    # Class variables go here
    db_name = "content_creator_schema" # Class attribute holding the schema name

    # self is effectively going to be a placeholder that holds all the info about the object you are creating
    def __init__(self, data): # data is a parameter holding a DICTIONARY!!
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.channel_name = data["channel_name"]
        self.genre = data["genre"]
        self.screen_name = data["screen_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.contents = [] # Placeholder to hold MANY Content objects

    # Use class methods to call on the database
    @classmethod
    def add_creator(cls, data): # data will hold form data mostly
        query = """
        INSERT INTO creators 
        (first_name, last_name, genre, screen_name, channel_name)
        VALUES (%(first_name)s, %(last_name)s, %(genre)s, %(screen_name)s, %(channel_name)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_creators(cls): # No data needed - the query doesn't need any values inserted
        query = """
        SELECT * FROM creators;
        """
        results = connectToMySQL(cls.db_name).query_db(query) # No data needed
        print(results)
        # Create a list of Creator objects (class instances)
        creator_object_list = []
        # Looping through a list of dictionaries - called "results"
        for creator_dictionary in results:
            print(creator_dictionary)
            # Make a new Creator object
            new_creator_object = cls(creator_dictionary) # cls means the class we're in, so cls() means in this case Creator()
            # Add this object to the list
            creator_object_list.append(new_creator_object)
        return creator_object_list # Watch your indentation!
    
    @classmethod
    def get_one_creator(cls, data): # Need data because the query needs a specific value - ID
        query = """
        SELECT * FROM creators WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        new_creator_object = cls(results[0]) # results is a list, results at index 0 is a dictionary, and we must pass in a dictionary
        return new_creator_object
    
    @classmethod
    def edit_one_creator(cls, data):
        query = """
        UPDATE creators SET
        first_name = %(first_name)s,
        last_name = %(last_name)s,
        genre = %(genre)s,
        screen_name = %(screen_name)s,
        channel_name = %(channel_name)s
        WHERE
        id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def delete_one_creator(cls, data):
        query = """
        DELETE FROM creators WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db_name).query_db(query, data)