from flask_app.config.mysqlconnection import connectToMySQL

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