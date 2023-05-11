# Class for Content Creators

class Creator: # Names of classes are actually in PascalCase - each word is capitalized; for example: ContentCreator
    # Class variables go here
    overseer = "Federal Communication Commission"

    # self is effectively going to be a placeholder that holds all the info about the object you are creating
    def __init__(self, first_name, last_name, channel_name, genre, screen_name): 
        self.first_name = first_name
        self.last_name = last_name
        self.channel_name = channel_name
        self.genre = genre
        self.screen_name = screen_name
        self.subscriber_count = 0 # Give everyone a default value of 0 here for subscriber count
        self.content = [] # Empty list that will hold all the Content made by this Creator - try to figure out how to add Content to this list on your own!

    # Instance method - a method tied to a specific class instance (specific object)
    def add_new_subscriber(self): # Don't forget self!
        self.subscriber_count += 1
        return self # Allow for chaining

    # Another instance method
    def rename_channel(self, new_channel_name): # Don't forget self!
        self.channel_name = new_channel_name # Use self inside the method here!
        return self # Allow for chaining
    
    @classmethod
    def rename_overseer(cls, new_name):
        cls.overseer = new_name

    @staticmethod
    def money_made(subscriber_count, fee):
        return subscriber_count*fee
    

class Content:
    def __init__(self, media_type, title, description, recorded_date, content_creator):
        self.media_type = media_type # Podcast, blog, video, picture
        self.title = title # What is the title of the podcast, blog, etc.?
        self.description = description
        self.recorded_date = recorded_date # When the content was created
        self.creator = content_creator # Link who made this Content
        

star_wars_fan = Creator("Luke", "Skywalker", "The Star Wars Blog", "Sci-Fi", "l_skywalker")
print(star_wars_fan.first_name) # To refer to attributes in an object, use the period "."

pokemon_fan = Creator("Ash", "Ketchum", "The Ultimate Trainer", "Gaming", "ash_k")
print(pokemon_fan.first_name + " " + pokemon_fan.last_name)

# Calling on methods
star_wars_fan.add_new_subscriber()
print(f"Number of subscribers for the Star Wars fan = {star_wars_fan.subscriber_count}")
print(f"Number of subscribers for the Pokemon fan = {pokemon_fan.subscriber_count}")

# Change the screen name from "ash_k" to "ash" directly
pokemon_fan.screen_name = "ash"

# Change the name of the channel for the Star Wars fan using a method
print("Original channel name: " + star_wars_fan.channel_name)
star_wars_fan.rename_channel("The Galaxy's Protector")
print("New channel name: " + star_wars_fan.channel_name)

# Chaining methods
star_wars_fan.add_new_subscriber().add_new_subscriber().add_new_subscriber().add_new_subscriber()
print(f"Number of subscribers for the Star Wars fan = {star_wars_fan.subscriber_count}")

# Test grabbing a class variable
print(Creator.overseer) # NameOfClass.name_of_class_variable

# Test class methods
Creator.rename_overseer("the new FCC") # NameOfClass.name_of_class_method()
print(Creator.overseer)

# Static method
print(Creator.money_made(200, 10))

# Create some content
new_review = Content("Video", "Review of The Force Awakens", "I talk about this movie in the sequel trilogy.", "2020-12-15", star_wars_fan)

# Display the first name of the creator from the new_review variable - your answer cannot be star_wars_fan.first_name
# IMPORTANT - grabbing stuff when linking classes
print(type(new_review.creator))
print(new_review.creator.first_name) 