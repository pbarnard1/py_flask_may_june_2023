from flask_app.config.mysqlconnection import connectToMySQL # Remember to import this for all your models so we can talk to DB

class Creator:
    # Class variables go here
    db_name = "content_creator_schema"

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
        self.contents = [] # Hold a bunch of Content objects

    # Use class methods to call on the database
    @classmethod
    def add_creator(cls, data): # data will hold form data mostly
        query = """
        INSERT INTO creators 
        (first_name, last_name, genre, screen_name, channel_name)
        VALUES (%(first_name)s, %(last_name)s, %(genre)s, %(screen_name)s, %(channel_name)s);
        """
        return connectToMySQL(cls.db_name).query_db(query, data)