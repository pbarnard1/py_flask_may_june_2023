from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import creator # Import the other model files as needed
class Content:
    db_name = "content_creator_schema" # Class attribute holding the schema name

    def __init__(self, data):
        self.id = data["id"]
        self.media_type = data["media_type"]
        self.description = data["description"]
        self.title = data["title"]
        self.recorded_date = data["recorded_date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.creator = None # Placeholder for holding ONE Creator

    @classmethod
    def add_content(cls, data):
        query = """
        INSERT INTO contents
        (media_type, description, title, recorded_date, creator_id)
        VALUES
        (%(media_type)s, %(description)s, %(title)s, %(recorded_date)s, %(creator_id)s);
        """ # Note the foreign key creator_id!!
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def get_all_content(cls):
        query = """
        SELECT * FROM contents
        JOIN creators
        ON contents.creator_id = creators.id;
        """
        results = connectToMySQL(cls.db_name).query_db(query)
        print(results)
        print(type(results))
        all_content_objects = [] # List of Content objects
        # Looping through each dictionary in our list of results from our query
        for each_content_dictionary in results:
            print(each_content_dictionary)
            # Make the Content object
            new_content_object = cls(each_content_dictionary) # cls() means Content() class as we're inside that right now
            # Make the Creator object
            # Need a new dictionary to remove the table names
            new_creator_dictionary = {
                "id": each_content_dictionary["creators.id"], # Table name added due to duplicate column
                "first_name": each_content_dictionary["first_name"],
                "last_name": each_content_dictionary["last_name"],
                "channel_name": each_content_dictionary["channel_name"],
                "genre": each_content_dictionary["genre"],
                "screen_name": each_content_dictionary["screen_name"],
                "created_at": each_content_dictionary["creators.created_at"], # Table name added due to duplicate column
                "updated_at": each_content_dictionary["creators.updated_at"], # Table name added due to duplicate column
            }
            new_creator_object = creator.Creator(new_creator_dictionary)
            # Link the Content and Creator
            new_content_object.creator = new_creator_object
            # Add this Content object to the list
            all_content_objects.append(new_content_object)
        return all_content_objects
    
    @classmethod
    def get_one_post(cls, data):
        query = """
        SELECT * FROM contents
        JOIN creators
        ON contents.creator_id = creators.id
        WHERE contents.id = %(id)s;
        """ # Make sure you reference the correct table in the where clause!!
        results = connectToMySQL(cls.db_name).query_db(query, data)
        print(results)
        print(type(results))
        print(results[0])
        print(type(results[0]))
        this_content_dictionary = results[0] # Grabbing the dictionary at index 0 from the list called "results"
        print(this_content_dictionary)
        # Make the Content object
        new_content_object = cls(this_content_dictionary) # cls() means Content() class as we're inside that right now
        # Make the Creator object
        # Need a new dictionary to remove the table names
        new_creator_dictionary = {
            "id": this_content_dictionary["creators.id"], # Table name added due to duplicate column
            "first_name": this_content_dictionary["first_name"],
            "last_name": this_content_dictionary["last_name"],
            "channel_name": this_content_dictionary["channel_name"],
            "genre": this_content_dictionary["genre"],
            "screen_name": this_content_dictionary["screen_name"],
            "created_at": this_content_dictionary["creators.created_at"], # Table name added due to duplicate column
            "updated_at": this_content_dictionary["creators.updated_at"], # Table name added due to duplicate column
        }
        new_creator_object = creator.Creator(new_creator_dictionary)
        # Link the Content and Creator
        new_content_object.creator = new_creator_object
        print(new_content_object.title) # Debugging to make sure we get the title correctly
        return new_content_object